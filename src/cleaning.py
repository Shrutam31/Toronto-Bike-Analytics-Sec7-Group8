import pandas as pd
import numpy as np

def clean_station_names(df):
    """
    Removes rows where 'Start Station Name' is missing or 'NULL'.
    """
    # 1. Drop actual NaNs
    df = df.dropna(subset=['Start Station Name'])

    # 2. Drop rows where the string is exactly "NULL"
    df = df[df['Start Station Name'] != 'NULL']

    return df