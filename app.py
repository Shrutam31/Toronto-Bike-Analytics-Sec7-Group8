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
    count_trips_by_hour  # <--- NEW IMPORT from Story 9
)

# 2. PAGE CONFIG
st.set_page_config(page_title="Toronto Bike Share Analytics", layout="wide")
st.title("🚴 Toronto Bike Share Analytics Tool")
st.markdown("**Sprint 2: Interactive Dashboard**")

FILE_PATH = "data/bike_data.csv"

# 3. LOAD & CLEAN DATA
df = load_data(FILE_PATH)

if df is None:
    st.error(f"❌ Error: File not found at `{FILE_PATH}`")
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
        st.warning("⚠️ No data matches your filters! Please adjust your selection.")
        st.stop()
        
    st.sidebar.success(f"Showing {len(filtered_df):,} trips")
    
    # ---------------------------------------------------------
    # DASHBOARD SECTIONS
    # ---------------------------------------------------------

    # 1. KEY METRICS (Story 5)
    st.subheader("1. Key Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Rows", f"{len(filtered_df):,}")
    with col2:
        st.metric("Total Columns", len(filtered_df.columns))
    with col3:
        annual_pct = calculate_user_type_percentage(filtered_df, "Annual Member")
        st.metric("Annual Member %", f"{annual_pct:.1f}%")

    # 2. TRIP DURATION BY MODEL (Story 6)
    st.subheader("2. Trip Duration by Model")
    m_col1, m_col2 = st.columns(2)
    
    with m_col1:
        avg_iconic = calculate_avg_duration_by_model(filtered_df, "ICONIC")
        st.metric("Avg Duration (ICONIC)", f"{avg_iconic:.1f} min")
        
    with m_col2:
        avg_efit = calculate_avg_duration_by_model(filtered_df, "EFIT G5")
        st.metric("Avg Duration (EFIT G5)", f"{avg_efit:.1f} min")

    # 3. TOP STATIONS CHART (Story 7)
    st.markdown("---")
    st.subheader("3. Most Popular Start Stations")
    
    top_stations_df = get_top_start_stations(filtered_df, n=10)
    
    if not top_stations_df.empty:
        fig = px.bar(
            top_stations_df,
            x='Trip Count',
            y='Start Station Name',
            orientation='h',
            text='Trip Count',
            title=f"Top 10 Start Stations ({selected_month})",
            color='Trip Count',
            color_continuous_scale='Blues'
        )
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=500)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Not enough data to show top stations.")

    # 4. PEAK USAGE HOURS (Story 9) <--- NEW SECTION
    st.markdown("---")
    st.subheader("4. Peak Usage Hours")
    
    hourly_data = count_trips_by_hour(filtered_df)
    
    if not hourly_data.empty:
        fig_hourly = px.bar(
            hourly_data,
            x='Hour',
            y='Trip Count',
            title=f"Trips by Hour of Day ({selected_month})",
            labels={'Hour': 'Hour of Day (0-23)', 'Trip Count': 'Number of Trips'},
            text='Trip Count'
        )
        fig_hourly.update_layout(
            xaxis=dict(tickmode='linear', tick0=0, dtick=1),
            height=450
        )
        st.plotly_chart(fig_hourly, use_container_width=True)
    else:
        st.info("Not enough data to show hourly patterns.")

    # 5. DATA PREVIEW
    st.markdown("---")
    with st.expander("📂 View Filtered Raw Data"):
        st.dataframe(filtered_df.head(100))