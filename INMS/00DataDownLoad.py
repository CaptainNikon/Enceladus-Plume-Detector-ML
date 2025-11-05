
"""
This script downloads data from the offical NASA Planetary Data System. 
We filter the directory for specific days, where an Enceladus plume flyby was carried out and detected by the INMS instrument.
We use a HTML parser to collect the CSV files for flyby day and download the data of the whole day.
"""

import os
import requests
from html.parser import HTMLParser

# Define flybys and their PDS directory paths
flybys = [
    {
        "name": "E3",
        "path": "2008/061_091_MAR/072",
    },
    {
        "name": "E5",
        "path": "2008/275_305_OCT/283",
    },
    {
        "name": "E7",
        "path": "2009/305_334_NOV/306",
    },
    {
        "name": "E14",
        "path": "2011/274_304_OCT/274",
    },
    {
        "name": "E17",
        "path": "2012/061_091_MAR/087",
    },
    {
        "name": "E18",
        "path": "2012/092_121_APR/105",
    },
    {
        "name": "E21",
        "path": "2015/274_304_OCT/301",
    },
]

BASE_URL = "https://pds-ppi.igpp.ucla.edu/data/CO-S-INMS-3-L1A-U-V1.0/DATA/SATURN/"

# Parse the links that are needed
class LinkParser(HTMLParser):
    """Extract all CSV file links from HTML"""
    def __init__(self):
        super().__init__()
        self.links = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href' and value.endswith('.CSV'):
                    self.links.append(value)


def download_day(flyby):
    """Download ALL CSV files from the entire day's directory"""
    
    flyby_name = flyby["name"]
    doy_path = flyby["path"]
    
    # Create output directory
    output_dir = f"INMS_data/{flyby_name}"
    os.makedirs(output_dir, exist_ok=True)

    # Start browser session
    print(f"Downloading INMS data for {flyby_name}")
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Python INMS Downloader)'
    })
    
    # Fetch directory url
    dir_url = f"{BASE_URL}{doy_path}/"
    try:
        print("Fetching directory...")
        response = session.get(dir_url, timeout=15)
        response.raise_for_status()
        
        # Parse HTML to extract all CSV links
        parser = LinkParser()
        parser.feed(response.text)
        
        if not parser.links:
            print("No CSV files found!")
            return 0, 0
        
        print(f"Found {len(parser.links)} CSV files\n")
        
        downloaded_count = 0
        failed_count = 0

        print("Starting download...")
        
        # Download all CSV files
        for i, filename in enumerate(parser.links, 1):
            file_url = f"{BASE_URL}{doy_path}/{filename}"
            filepath = os.path.join(output_dir, filename)
            
            print(f"[{i:3d}/{len(parser.links)}] {filename}...", end=" ", flush=True)
            
            try:
                file_response = session.get(file_url, timeout=30)
                file_response.raise_for_status()
                
                with open(filepath, 'wb') as f:
                    f.write(file_response.content)
                downloaded_count += 1
                
            except Exception as e:
                print(f"{str(e)}")
                failed_count += 1

        print(f"\n  Summary: {downloaded_count} files downloaded, {failed_count} failed")
        return downloaded_count, failed_count
    
    except Exception as e:
        print(f"Error accessing directory: {str(e)}")
        return 0, len(parser.links) if 'parser' in locals() else 0

# Main execution
if __name__ == "__main__":
    total_downloaded = 0
    total_failed = 0
    total_size = 0
    
    print("Starting INMS Data Downloader")
    
    for flyby in flybys:
        try:
            downloaded, failed = download_day(flyby)
            total_downloaded += downloaded
            total_failed += failed
        except Exception as e:
            print(f"\nError processing {flyby['name']}: {str(e)}")
    
    print(f"\n{'='*80}")
    print(f"Summary")
    print(f"{'='*80}")
    print(f"Total files downloaded: {total_downloaded}")
    print(f"Total files failed:     {total_failed}")
    print(f"Output directory:       ./INMS_data/")
    print(f"{'='*80}\n")