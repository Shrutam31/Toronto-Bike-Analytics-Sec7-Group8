# Toronto-Bike-Analytics-Sec7-Group8
Agile project for analyzing Toronto Bike Share data
# 🚴 Toronto Bike Share Analytics Tool

## 📋 Project Overview
This tool is an interactive dashboard designed to analyze ridership data for the Toronto Bike Share network. Built using **Python** and **Streamlit**, it allows data analysts and city planners to visualize usage patterns, identify popular stations, and compare bike model performance.

### Key Features
* **Data Ingestion:** Loads and cleans large CSV datasets (~900k rows).
* **Interactive Filtering:** Filter data by Month and Bike Model.
* **Key Metrics:** Dynamic calculation of User Type distribution (Annual vs. Casual).
* **Visualizations:**
    * Top 10 Start Stations (Horizontal Bar Chart).
    * Peak Usage Hours (Hourly Bar Chart).
* **Export:** Download filtered data for offline analysis.

---

## 🛠️ Technical Architecture
* **Language:** Python 3.9+
* **Framework:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Visualization:** Plotly Express
* **Testing:** Pytest (TDD Approach)

---

## 🚀 How to Run the Project

### 1. Prerequisites
Ensure you have Python installed. Clone the repository:
```bash
git clone https://github.com/Shrutam31/toronto-bike-analytics.git
cd toronto-bike-analytics


# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py

pytest