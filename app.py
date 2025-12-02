import streamlit as st
import pandas as pd
# 1. NEW IMPORT
from src.loader import load_data
from src.cleaning import clean_station_names, process_datetime_columns
from src.analysis import calculate_user_type_percentage

from src.analysis import calculate_user_type_percentage, calculate_avg_duration_by_model

st.set_page_config(page_title="Toronto Bike Share Analytics", layout="wide")
st.title("🚴 Toronto Bike Share Analytics Tool")
st.markdown("**Sprint 1: Data Engineering & Inspection**")

FILE_PATH = "data/bike_data.csv"

st.subheader("1. Data Loading Status")

# 2. REFACTORED LOGIC: Call the function instead of writing raw code
df = load_data(FILE_PATH)

if df is None:
    st.error(f"❌ Error: File not found at `{FILE_PATH}`")
    st.stop()
else:
    # Apply cleaning (from previous stories)
    df = clean_station_names(df)
    df = process_datetime_columns(df)
    
    st.success(f"✅ Successfully loaded data from `{FILE_PATH}`")
    
    # Display Metrics
    st.subheader("1. Key Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Rows", f"{len(df):,}")
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        # DYNAMIC CALCULATION
        annual_pct = calculate_user_type_percentage(df, "Annual Member")
        st.metric("Annual Member %", f"{annual_pct:.1f}%")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Rows", f"{len(df):,}")
    with col2:
        st.metric("Total Columns", len(df.columns))

    st.subheader("2. Raw Data Preview")
    st.dataframe(df.head())

    st.subheader("2. Trip Duration by Model")
    m_col1, m_col2 = st.columns(2)
    
    with m_col1:
        avg_iconic = calculate_avg_duration_by_model(df, "ICONIC")
        st.metric("Avg Duration (ICONIC)", f"{avg_iconic:.1f} min")
        
    with m_col2:
        avg_efit = calculate_avg_duration_by_model(df, "EFIT G5")
        st.metric("Avg Duration (EFIT G5)", f"{avg_efit:.1f} min")
    
    # Verify Columns
    st.subheader("3. Column Verification")
    required_cols = ["Trip Id", "Start Time", "User Type"]
    missing = [c for c in required_cols if c not in df.columns]
    
    if missing:
        st.warning(f"⚠️ Missing expected columns: {missing}")
    else:
        st.success("✅ Critical columns found.")