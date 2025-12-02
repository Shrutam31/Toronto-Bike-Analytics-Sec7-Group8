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

def calculate_avg_duration_by_model(df, model_name):
    """
    Calculates the average trip duration for a specific bike model in MINUTES.
    
    Args:
        df (pd.DataFrame): Dataframe with 'Model' and 'Trip Duration'.
        model_name (str): The model name (e.g., 'ICONIC').
        
    Returns:
        float: Average duration in minutes.
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