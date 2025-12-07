import streamlit as st
import pandas as pd
import plotly.express as px

# 1. IMPORTS
from src.loader import load_data
from src.cleaning import clean_station_names, process_datetime_columns
from src.analysis import (
    calculate_user_type_percentage, 
    calculate_avg_duration_by_model,
    get_top_start_stations,
    count_trips_by_hour  # <--- THIS WAS MISSING
)
from src.visualization import plot_top_stations, plot_peak_hours

# 2. PAGE CONFIG
st.set_page_config(page_title="Toronto Bike Share Analytics", layout="wide")
st.title("🚴 Toronto Bike Share Analytics Tool")
st.markdown("*Sprint 2: Interactive Dashboard*")

FILE_PATH = "data/bike_data.csv"

# 3. LOAD & CLEAN DATA
df = load_data(FILE_PATH)

if df is None:
    st.error(f"❌ Error: File not found at {FILE_PATH}")
    st.stop()
else:
    # Apply cleaning
    df = clean_station_names(df)
    df = process_datetime_columns(df)

    # --- USER STORY 8: SIDEBAR FILTERS ---
    st.sidebar.header("🔍 Filters")

    # A. Month Filter
    available_months = df['Month'].unique().tolist()
    selected_month = st.sidebar.selectbox("Select Month", available_months)

    # B. Model Filter
    available_models = df['Model'].unique().tolist()
    selected_models = st.sidebar.multiselect("Select Bike Model", available_models, default=available_models)

    # C. Apply Filters (Creating filtered_df)
    filtered_df = df[
        (df['Month'] == selected_month) &
        (df['Model'].isin(selected_models))
    ]

    # Show warning if empty
    if filtered_df.empty:
        st.warning("⚠ No data matches your filters! Please adjust your selection.")
        st.stop()
        
    st.sidebar.success(f"Showing {len(filtered_df):,} trips")
    
    # ---------------------------------------------------------
    # DASHBOARD SECTIONS (Now using filtered_df)
    # ---------------------------------------------------------

    # 1. KEY METRICS (Story 5)
    st.subheader("1. Key Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # UPDATED: Use filtered_df
        st.metric("Total Rows", f"{len(filtered_df):,}")
    with col2:
        # Columns don't change, so df is fine, but technically filtered_df works too
        st.metric("Total Columns", len(filtered_df.columns))
    with col3:
        # UPDATED: Use filtered_df for dynamic percentage
        annual_pct = calculate_user_type_percentage(filtered_df, "Annual Member")
        st.metric("Annual Member %", f"{annual_pct:.1f}%")

    # 2. TRIP DURATION BY MODEL (Story 6)
    # (Restored this section so your app is complete)
    st.subheader("2. Trip Duration by Model")
    m_col1, m_col2 = st.columns(2)
    
    with m_col1:
        # UPDATED: Use filtered_df
        avg_iconic = calculate_avg_duration_by_model(filtered_df, "ICONIC")
        st.metric("Avg Duration (ICONIC)", f"{avg_iconic:.1f} min")
        
    with m_col2:
        # UPDATED: Use filtered_df
        avg_efit = calculate_avg_duration_by_model(filtered_df, "EFIT G5")
        st.metric("Avg Duration (EFIT G5)", f"{avg_efit:.1f} min")

    # 3. TOP STATIONS CHART (Refactored)
    st.markdown("---")
    st.subheader("3. Most Popular Start Stations")
    
    top_stations_df = get_top_start_stations(filtered_df, n=10)
    
    # CALL THE NEW FUNCTION
    fig_stations = plot_top_stations(top_stations_df, title_suffix=f"({selected_month})")
    
    if fig_stations:
        st.plotly_chart(fig_stations, use_container_width=True)
    else:
        st.info("Not enough data to show top stations.")

    # 4. PEAK USAGE HOURS (Refactored)
    st.markdown("---")
    st.subheader("4. Peak Usage Hours")
    
    hourly_data = count_trips_by_hour(filtered_df)
    
    # CALL THE NEW FUNCTION
    fig_hourly = plot_peak_hours(hourly_data, title_suffix=f"({selected_month})")
    
    if fig_hourly:
        st.plotly_chart(fig_hourly, use_container_width=True)
    else:
        st.info("Not enough data to show hourly patterns.")

    # 5. DATA PREVIEW & DOWNLOAD (User Story 10)
    st.markdown("---")
    st.subheader("5. Data Export")
    
    with st.expander("📂 View Filtered Raw Data", expanded=True):
        # Show the data first
        st.dataframe(filtered_df.head(100))
        
        # LOGIC FOR DOWNLOAD (Task #46 & #47)
        # Convert dataframe to CSV string
        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        
        # Create the filename dynamically based on the month
        file_name = f"bike_share_data_{selected_month}.csv"
        
        st.download_button(
            label="📥 Download Filtered CSV",
            data=csv_data,
            file_name=file_name,
            mime="text/csv",
            help="Download the currently filtered dataset for offline analysis."
        )