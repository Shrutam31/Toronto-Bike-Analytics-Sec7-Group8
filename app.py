import streamlit as st
import pandas as pd
import os

# ------------------------------------------------------------------
# [User Story 1] Load Raw Data & Inspect Structure
# Description: Load CSV and display basic structure to verify data integrity.
# ------------------------------------------------------------------

# 1. Page Configuration (Task #13)
st.set_page_config(page_title="Toronto Bike Share Analytics", layout="wide")
st.title("🚴 Toronto Bike Share Analytics Tool")
st.markdown("**Sprint 1: Data Engineering & Inspection**")

# 2. Define File Path
# Note: We assume the file is in the 'data' folder as per the repo structure
FILE_PATH = "data/bike_data.csv"

# 3. Load Data Logic (Task #14)
st.subheader("1. Data Loading Status")

if not os.path.exists(FILE_PATH):
    st.error(f"❌ Error: File not found at `{FILE_PATH}`")
    st.info("Please ensure your CSV file is renamed to 'bike_data.csv' and placed in the 'data/' folder.")
    st.stop()
else:
    try:
        # Load the dataframe
        df = pd.read_csv(FILE_PATH)
        st.success(f"✅ Successfully loaded data from `{FILE_PATH}`")
        
        # 4. Display Metrics & Preview (Task #15)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Rows", f"{len(df):,}")
        with col2:
            st.metric("Total Columns", len(df.columns))

        st.subheader("2. Raw Data Preview")
        st.caption("First 5 rows of the dataset:")
        st.dataframe(df.head())

        # 5. Verify Critical Columns
        st.subheader("3. Column Verification")
        required_cols = ["Trip Id", "Start Time", "User Type"]
        available_cols = df.columns.tolist()
        
        missing = [c for c in required_cols if c not in available_cols]
        
        if missing:
            st.warning(f"⚠️ Missing expected columns: {missing}")
        else:
            st.success("✅ Critical columns (Trip Id, Start Time, User Type) found.")
            
        with st.expander("View All Column Names"):
            st.write(available_cols)

    except Exception as e:
        st.error(f"❌ An error occurred while reading the file: {e}")