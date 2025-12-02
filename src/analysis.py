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