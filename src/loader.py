import pandas as pd
import os

def load_data(file_path):
    """
    Loads the bike share data from a CSV file.
    
    Args:
        file_path (str): The relative path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded dataframe, or None if file not found.
    """
    if not os.path.exists(file_path):
        return None
        
    try:
        df = pd.read_csv(file_path)
        
        # TASK #28: Fix column naming inconsistencies
        # The raw data sometimes has "Trip  Duration" (two spaces)
        if "Trip  Duration" in df.columns:
            df.rename(columns={"Trip  Duration": "Trip Duration"}, inplace=True)
            
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None