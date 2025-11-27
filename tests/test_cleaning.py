import pytest
import pandas as pd
import numpy as np

from src.cleaning import clean_station_names

def test_remove_null_station_names():
    
    data = {
        'Trip Id': [1, 2, 3],
        'Start Station Name': ['Union Station', 'NULL', np.nan]
    }
    df = pd.DataFrame(data)

    #  Run the cleaning function
    cleaned_df = clean_station_names(df)

    assert len(cleaned_df) == 1
    assert cleaned_df.iloc[0]['Start Station Name'] == 'Union Station'