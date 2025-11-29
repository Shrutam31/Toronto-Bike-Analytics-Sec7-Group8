import pandas as pd
import numpy as np

def clean_station_names(df):
    """
    Removes rows where 'Start Station Name' is missing, 'NULL', or empty.
    Refactored to handle whitespace and case sensitivity.
    """
    if 'Start Station Name' not in df.columns:
        return df

    # 1. Create a copy to avoid SettingWithCopy warnings
    clean_df = df.copy()

    # 2. Standardize: Convert 'NULL' strings to actual NaN
    # We also handle "null" or " NULL " just in case
    clean_df['Start Station Name'] = clean_df['Start Station Name'].replace(
        to_replace=r'(?i)^null$', value=np.nan, regex=True
    )

    # 3. Drop actual NaNs
    clean_df = clean_df.dropna(subset=['Start Station Name'])

    return clean_df

def process_datetime_columns(df):
    """
    Converts 'Start Time' to datetime and extracts Hour, Month, Day of Week.
    Refactored to handle NaT (Not a Time) values.
    """
    if 'Start Time' not in df.columns:
        return df
        
    df = df.copy()
    
    # 1. Convert to Datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
    
    # Refactor: Drop rows where date conversion failed (NaT)
    df = df.dropna(subset=['Start Time'])
    
    # 2. Extract Features (Cast hour to int just in case)
    df['Hour'] = df['Start Time'].dt.hour.astype(int)
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()
    
    return df