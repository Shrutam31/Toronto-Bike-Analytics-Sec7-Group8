import pytest
import pandas as pd
import numpy as np

from src.cleaning import clean_station_names
from src.cleaning import process_datetime_columns

def test_remove_null_station_names():
    
    data = {
        'Trip Id': [1, 2, 3],
        'Start Station Name': ['Union Station', 'NULL', np.nan]
    }
    df = pd.DataFrame(data)

    cleaned_df = clean_station_names(df)

    assert len(cleaned_df) == 1
    assert cleaned_df.iloc[0]['Start Station Name'] == 'Union Station'

def test_process_datetime_columns_extracts_features():
    # 1. SETUP: Create data with string dates (MM/DD/YYYY HH:MM)
    data = {
        'Trip Id': [101, 102],
        'Start Time': ['08/01/2024 08:30', '08/01/2024 18:45']
    }
    df = pd.DataFrame(data)

    # 2. ACT: Run the date processing function
    processed_df = process_datetime_columns(df)

    # 3. ASSERT: Check if new columns exist and are correct
    assert 'Hour' in processed_df.columns
    assert 'Month' in processed_df.columns
    assert 'Day of Week' in processed_df.columns
    
    # Check specific values (8:30 AM is hour 8)
    assert processed_df.iloc[0]['Hour'] == 8
    assert processed_df.iloc[0]['Month'] == 'August'