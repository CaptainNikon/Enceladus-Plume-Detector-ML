"""
This script import all downloaded CSV files, while skipping the house keeping rows and focussing on the essential ones.
Data 60 mintues before and after the closest approach to Enceladus is loaded into a combined dataframe and CSV.
"""

import pandas as pd
import numpy as np
import os
import glob
from datetime import datetime, timedelta

# Define flyby date and closest approach time
FLYBYS = {
    "E3": {"date": "2008-03-12", "doy": 72, "ca_time": "19:07:00"},
    "E5": {"date": "2008-10-09", "doy": 283, "ca_time": "19:07:15"},
    "E7": {"date": "2009-11-02", "doy": 306, "ca_time": "07:42:05"},
    "E14": {"date": "2011-10-01", "doy": 274, "ca_time": "13:52:35"},
    "E17": {"date": "2012-03-27", "doy": 87, "ca_time": "18:30:15"},
    "E18": {"date": "2012-04-14", "doy": 105, "ca_time": "14:01:37"},
    "E21": {"date": "2015-10-28", "doy": 301, "ca_time": "15:22:46"},
}


ESSENTIAL_COLUMNS = [
    # Spacecraft time clock in UTC
    "sclk",

    # Target geometry: Positon, Spacecraft altitude above target
    "targ_pos_x", "targ_pos_y", "targ_pos_z", "alt_t",

    # Spacecraft velocity: combined, x, y, z
    "velocity_comp", "sc_vel_t_x", "sc_vel_t_y", "sc_vel_t_z",

    # View geometry: Viewing direction, spacecraft position, distance to Saturn
    'view_dir_t_x', 'view_dir_t_y', 'view_dir_t_z',
    'sc_pos_t_x', 'sc_pos_t_y', 'sc_pos_t_z',
    "distance_s"

    # Mass-spectrometer, Detector counts
    "mass_per_charge", "c1counts", "c2counts",

    # Coadd count and operating mode
    "coadd_cnt", "source"
]


def load_inms(filepath):
    """Load CSV files"""
    try:
        df = pd.read_csv(
            filepath, 
            sep=',',
            skiprows=[1, 2],
            header=0,
            low_memory=False,
            usecols=lambda col: col.strip() in ESSENTIAL_COLUMNS
        )
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        return None

def sclk_to_datetime(sclk_str):
    """Convert Cassini SCLK string (YYYY-DDDTHH:MM:SS.sss) to datetime"""
    return datetime.strptime(sclk_str, '%Y-%jT%H:%M:%S.%f')


def load_slim_inms_data(base_dir="../../INMS_data", time_window_hours=1):
    """Load data within ±time_window_hours of each flyby"""

    print(f"Loading INMS DATA (±{time_window_hours} hour window)")

    all_data = []
    
    for flyby_name in sorted(FLYBYS.keys()):
        flyby_dir = os.path.join(base_dir, flyby_name)
        
        if not os.path.exists(flyby_dir):
            continue
        
        csv_files = sorted(glob.glob(os.path.join(flyby_dir, "*.CSV")))
        if not csv_files:
            continue
        
        # Get CA time
        ca_time = datetime.strptime(
            f"{FLYBYS[flyby_name]['date']} {FLYBYS[flyby_name]['ca_time']}", 
            "%Y-%m-%d %H:%M:%S"
        )
        
        # Define time window
        window_start = ca_time - timedelta(hours=time_window_hours)
        window_end = ca_time + timedelta(hours=time_window_hours)
        
        
        flyby_data = []
        loaded_files = 0

        print("Per flyby: \n")
        
        for filepath in csv_files:
           
            df = load_inms(filepath)
            if df is None or df.empty:
                continue

            # Create new parsed timestamp column
            df['TIME'] = df['sclk'].apply(sclk_to_datetime)

            # Filter rows within the time window
            df = df[(df['TIME'] >= window_start) & (df['TIME'] <= window_end)]

            if df.empty:
                continue

            # Add metadata
            df['FLYBY'] = flyby_name                                                # Flyby name
            df['TIME_FROM_CA'] = (df['TIME'] - ca_time).dt.total_seconds() / 60     # Time from closest approach
            df['TRAINING_SUBSET'] = np.abs(df['TIME_FROM_CA']) <= 10                # Smaller 10min window for training

            flyby_data.append(df)
            loaded_files += 1

        
        if flyby_data:
            flyby_df = pd.concat(flyby_data, ignore_index=True)
            all_data.append(flyby_df)
            plume_count = len(flyby_df[flyby_df['TRAINING_SUBSET']])
            print(f"{len(flyby_df):8,} rows ({loaded_files:2d} files, {plume_count:6,} plume)")
        else:
            print("No data in time window!")
    
    if not all_data:
        print("\n No data loaded!")
        return None
    
    print("Combining...")
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df = combined_df.sort_values(['FLYBY', 'TIME_FROM_CA']).reset_index(drop=True)
    
    print(f"Total: {len(combined_df):,} rows, {len(combined_df.columns)} columns")
    
    return combined_df



def save_csv(df):
    """Saving the dataframe to CSV"""

    print("Saving dataset")
    csv_path = "00FinalProject/INMS/CompiledDataSet/INMS_V0.csv"
    df.to_csv(csv_path, index=False)



def summary_statistics(df):
    """Quick summary"""
    
    print("="*90)
    print("Dataset summary")
    print("="*90)
    
    print("Per-flyby:")
    print("-" * 90)
    for flyby in sorted(df['FLYBY'].unique()):
        flyby_df = df[df['FLYBY'] == flyby]
        total = len(flyby_df)
        plume = len(flyby_df[flyby_df['TRAINING_SUBSET']])
        pct = (plume / total * 100) if total > 0 else 0
        
        # Count non-null c1counts as proxy for valid data
        valid_data = flyby_df['c1counts'].notna().sum() if 'c1counts' in flyby_df.columns else total
        
        print(f"  {flyby}: {total:8,} rows | {plume:6,} plume ({pct:4.1f}%) | {valid_data:8,} valid")
    
    print()
    print(f"Columns: {list(df.columns)}")
    print()



# Main execution
if __name__ == "__main__":

    df = load_slim_inms_data("INMS_data", time_window_hours=1)
    
    if df is not None:
        summary_statistics(df)
        save_csv(df)
        print("Done!")