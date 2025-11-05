import pandas as pd
import numpy as np
import os

def load_and_parse(input_path):
    df = pd.read_csv(input_path)
    df['TIME'] = pd.to_datetime(df['sclk'], format='%Y-%jT%H:%M:%S.%f', errors='coerce')
    return df

def clean_data(df):
    # Keep only rows with coadd_cnt == 1
    df_clean = df[df['coadd_cnt'] == 1].copy()
    df_clean = df_clean.drop(columns=['coadd_cnt'])
    
    # Remove single huge outlier in mass to charge
    df_clean = df_clean[df_clean['mass_per_charge'] < 150]

    # Clip velocity_comp
    q_low = df["velocity_comp"].quantile(0.01)
    q_high = df["velocity_comp"].quantile(0.99)
    df['velocity_comp'] = df['velocity_comp'].clip(lower=q_low, upper=q_high)

    # Remove rows where all geometry features are missing
    geometry_features = [
        'targ_pos_x', 'targ_pos_y', 'targ_pos_z', 'alt_t',
        'view_dir_t_x', 'view_dir_t_y', 'view_dir_t_z',
        'sc_pos_t_x', 'sc_pos_t_y', 'sc_pos_t_z',
        'sc_vel_t_x', 'sc_vel_t_y', 'sc_vel_t_z'
    ]
    all_nan_mask = df_clean[geometry_features].isnull().all(axis=1)
    df_clean = df_clean[~all_nan_mask].copy()
    return df_clean

def transform_features(df):
    # Log-transform for skewed/plume features
    df['c1counts'] = np.log1p(df['c1counts'])
    df['c2counts'] = np.log1p(df['c2counts'])
    return df

def drop_highly_correlated(df, threshold=0.90):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr().abs()
    np.fill_diagonal(corr_matrix.values, 0)
    to_drop = set()
    for col in corr_matrix.columns:
        if any(corr_matrix[col] > threshold):
            to_drop.add(col)
    print(f"Highly correlated columns: (corr > {threshold:.2f}): {sorted(list(to_drop))}")
    df_reduced = df.drop(columns=list(to_drop))
    return df_reduced


def plume_labels(df, window=0.5):
    df['PLUME'] = ((df['TIME_FROM_CA'] >= -window) & (df['TIME_FROM_CA'] <= window)).astype(int)
    print(df['PLUME'].value_counts())
    return df

def main():
    input_path = 'CompiledDataSet/INMS_V0.csv'
    output_path = 'CompiledDataSet/INMS_V1.csv'
    print("Loading and parsing data…")
    df = load_and_parse(input_path)
    print("Cleaning and filtering data…")
    df_clean = clean_data(df)
    print("Applying feature transformations…")
    df_clean = transform_features(df_clean)
    print("Dropping highly correlated columns…")
    df_final = drop_highly_correlated(df_clean)
    print("Adding plume labels")
    df_master = plume_labels(df_final)
    print(f"Saving cleaned data to {output_path}")
    df_master.to_csv(output_path, index=False)
    print("Done.")

if __name__ == "__main__":
    main()