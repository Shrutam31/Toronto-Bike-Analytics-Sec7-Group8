import pytest
import pandas as pd
# Import the function we haven't written yet
from src.analysis import calculate_user_type_percentage

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