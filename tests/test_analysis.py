import pytest
import pandas as pd
# Import the function we haven't written yet
from src.analysis import calculate_user_type_percentage
from src.analysis import calculate_avg_duration_by_model

def test_calculate_user_type_percentage_exact_match():
    # 1. SETUP: Create mixed data
    # Scenario: 4 trips total. 3 are 'Annual Member', 1 is 'Casual Member'.
    # Expected Result: 75% Annual.
    data = {
        'Trip Id': [1, 2, 3, 4],
        'User Type': ['Annual Member', 'Annual Member', 'Annual Member', 'Casual Member']
    }
    df = pd.DataFrame(data)

    # 2. ACT: Calculate percentage for 'Annual Member'
    result = calculate_user_type_percentage(df, user_type='Annual Member')

    # 3. ASSERT: Should be 75.0 exactly
    # Note: If the code used the buggy "contains('Member')" logic, this would be 100.0 and fail.
    assert result == 75.0

def test_calculate_user_type_percentage_empty():
    # Edge case: Empty dataframe
    df = pd.DataFrame({'Trip Id': [], 'User Type': []})
    result = calculate_user_type_percentage(df, 'Annual Member')
    assert result == 0.0

def test_calculate_avg_duration_converts_seconds_to_minutes():
    # 1. SETUP: Create data
    # 'Trip Duration' is usually in seconds in raw data.
    # Row 1: 120 seconds (2 mins)
    # Row 2: 240 seconds (4 mins)
    # Average should be 3 minutes.
    data = {
        'Model': ['ICONIC', 'ICONIC', 'EFIT G5'],
        'Trip Duration': [120, 240, 9999] 
    }
    df = pd.DataFrame(data)

    # 2. ACT: Calculate for ICONIC
    avg_minutes = calculate_avg_duration_by_model(df, 'ICONIC')

    # 3. ASSERT: Should be 3.0 minutes
    assert avg_minutes == 3.0

def test_calculate_avg_duration_handles_missing_model():
    # Edge Case: Model doesn't exist in data
    df = pd.DataFrame({'Model': ['A'], 'Trip Duration': [100]})
    result = calculate_avg_duration_by_model(df, 'ICONIC')
    assert result == 0.0