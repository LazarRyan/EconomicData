import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from fredapi import Fred
import pandas as pd
import io
import os
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Economic Data Dashboard", layout="wide")

# FRED API setup
FRED_API_KEY = os.environ.get('FRED_API_KEY')
fred = Fred(api_key=FRED_API_KEY)

# Helper functions
def get_fred_data(series_id, start_date=None, end_date=None):
    try:
        data = fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
        return data
    except Exception as e:
        st.error(f"Error fetching data for series {series_id}: {e}")
        return None

def calculate_yoy_change(series):
    return series.pct_change(periods=12)

def stock_market_formatter(x, p):
    if x >= 1e6:
        return f'${x/1e6:.1f}M'
    elif x >= 1e3:
        return f'${x/1e3:.0f}K'
    else:
        return f'${x:.0f}'

def plot_section(ax, title, categories, y_unit='', start_date=None, end_date=None, scale='linear', yoy_change=False):
    # ... (keep the plot_section function as it is in economic_data_visualizer.py)

def create_plot(start_date=None, end_date=None):
    plt.style.use('ggplot')
    fig, axs = plt.subplots(4, 2, figsize=(20, 30))
    fig.suptitle("Economic Data Visualization (FRED Data)", fontsize=24, fontweight='bold')

    categories = {
        # ... (keep the categories dictionary as it is)
    }

    y_units = {
        # ... (keep the y_units dictionary as it is)
    }

    scales = {
        # ... (keep the scales dictionary as it is)
    }

    yoy_change = {
        # ... (keep the yoy_change dictionary as it is)
    }

    for i, (title, category) in enumerate(categories.items()):
        plot_section(axs[i//2, i%2], title, category, y_units[title], start_date, end_date, scale=scales[title], yoy_change=yoy_change[title])

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig

# Streamlit app
st.title("Economic Data Dashboard")
st.write("Real-time insights into key economic indicators")

st.write("Welcome to our Economic Data Dashboard. This tool provides a comprehensive overview of various economic indicators, helping you stay informed about the current state of the economy. The data is sourced from the Federal Reserve Economic Data (FRED) and is updated regularly.")

# Date range selection
date_range = st.radio("Select Date Range", ["Full History", "Last 10 Years"])

if date_range == "Full History":
    fig = create_plot()
else:
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*10)
    fig = create_plot(start_date, end_date)

# Display the plot
st.pyplot(fig)

# Add a refresh button
if st.button("Refresh Data"):
    st.experimental_rerun()
