import pandas as pd

def calculate_user_type_percentage(df, user_type):
    """
    Calculates the percentage of trips made by a specific user type.
    
    Args:
        df (pd.DataFrame): Dataframe containing 'User Type'.
        user_type (str): The specific type to count (e.g., 'Annual Member').
        
    Returns:
        float: Percentage between 0.0 and 100.0
    """
    if df.empty or 'User Type' not in df.columns:
        return 0.0
        
    total_trips = len(df)
    
    # LOGIC FIX: Use exact matching (==), NOT .str.contains()
    # This prevents 'Casual Member' from being counted as an 'Annual Member'
    type_count = len(df[df['User Type'] == user_type])
    
    return (type_count / total_trips) * 100

def get_top_start_stations(df, n=10):
    """
    Identifies the top N most popular start stations.
    
    Args:
        df (pd.DataFrame): The dataframe.
        n (int): Number of stations to return.
        
    Returns:
        pd.DataFrame: A dataframe with 'Start Station Name' and 'Trip Count'.
    """
    if df.empty or 'Start Station Name' not in df.columns:
        return pd.DataFrame(columns=['Start Station Name', 'Trip Count'])
    
    # Group by station and count rows
    station_counts = df['Start Station Name'].value_counts().reset_index()
    station_counts.columns = ['Start Station Name', 'Trip Count']
    
    # Return top N
    return station_counts.head(n)
def calculate_avg_duration_by_model(df, model_name):
    """
    Calculates the average trip duration for a specific bike model in MINUTES.
    """
    # Safety checks
    if df.empty or 'Model' not in df.columns or 'Trip Duration' not in df.columns:
        return 0.0
        
    # Filter by model
    model_df = df[df['Model'] == model_name]
    
    if model_df.empty:
        return 0.0
        
    # Calculate mean in seconds
    avg_seconds = model_df['Trip Duration'].mean()
    
    # Convert to minutes
    return avg_seconds / 60

def count_trips_by_hour(df):
    """
    Counts the number of trips for each hour of the day (0-23).
    Returns a dataframe sorted by Hour.
    """
    if df.empty or 'Hour' not in df.columns:
        return pd.DataFrame(columns=['Hour', 'Trip Count'])
    
    # Group by Hour and count
    hourly_counts = df['Hour'].value_counts().reset_index()
    hourly_counts.columns = ['Hour', 'Trip Count']
    
    # Sort by Hour (0 to 23) naturally so the chart is chronological
    hourly_counts = hourly_counts.sort_values('Hour')
    
    return hourly_counts