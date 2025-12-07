import pandas as pd

def calculate_user_type_percentage(df, user_type):
    """
    Calculates the percentage of trips made by a specific user type.
    """
    if df.empty or 'User Type' not in df.columns:
        return 0.0
        
    total_trips = len(df)
    type_count = len(df[df['User Type'] == user_type])
    
    return (type_count / total_trips) * 100

def get_top_start_stations(df, n=10):
    """
    Identifies the top N most popular start stations.
    """
    if df.empty or 'Start Station Name' not in df.columns:
        return pd.DataFrame(columns=['Start Station Name', 'Trip Count'])
    
    station_counts = df['Start Station Name'].value_counts().reset_index()
    station_counts.columns = ['Start Station Name', 'Trip Count']
    return station_counts.head(n)

def calculate_avg_duration_by_model(df, model_name):
    """
    Calculates the average trip duration for a specific bike model in MINUTES.
    """
    if df.empty or 'Model' not in df.columns or 'Trip Duration' not in df.columns:
        return 0.0
        
    model_df = df[df['Model'] == model_name]
    
    if model_df.empty:
        return 0.0
        
    avg_seconds = model_df['Trip Duration'].mean()
    
    # RE-TYPED LINE TO FIX HIDDEN CHARACTER ERROR:
    return avg_seconds / 60

def count_trips_by_hour(df):
    """
    Counts the number of trips for each hour of the day (0-23).
    """
    if df.empty or 'Hour' not in df.columns:
        return pd.DataFrame(columns=['Hour', 'Trip Count'])
    
    hourly_counts = df['Hour'].value_counts().reset_index()
    hourly_counts.columns = ['Hour', 'Trip Count']
    hourly_counts = hourly_counts.sort_values('Hour')
    
    return hourly_counts