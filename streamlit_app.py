import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import numpy as np
from fredapi import Fred
import pandas as pd
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Economic Data Dashboard", layout="wide")

# FRED API setup
FRED_API_KEY = st.secrets["FRED_API_KEY"]
fred = Fred(api_key=FRED_API_KEY)

def get_fred_data(series_id, start_date=None, end_date=None):
    try:
        data = fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
        return data
    except Exception as e:
        st.error(f"Error fetching data for series {series_id}: {e}")
        return None

def calculate_yoy_change(series):
    return series.pct_change(periods=12)

def custom_formatter(x, p):
    if abs(x) >= 1e9:
        return f'{x/1e9:.1f}B'
    elif abs(x) >= 1e6:
        return f'{x/1e6:.1f}M'
    elif abs(x) >= 1e3:
        return f'{x/1e3:.1f}K'
    else:
        return f'{x:.1f}'

def plot_section(ax, title, categories, y_unit='', start_date=None, end_date=None, scale='linear', yoy_change=False):
    data = {}
    for label, series_id in categories.items():
        series_data = get_fred_data(series_id, start_date, end_date)
        if series_data is not None and len(series_data) > 0:
            if yoy_change:
                series_data = calculate_yoy_change(series_data)
            data[label] = series_data
        else:
            st.warning(f"No data available for {label} ({series_id})")

    if not data:
        ax.text(0.5, 0.5, "No data available", ha='center', va='center')
        return

    df = pd.DataFrame(data)
    df = df.dropna()  # Remove rows with missing data
    
    if scale == 'log':
        ax.set_yscale('log')
    else:
        ax.set_yscale('linear')
    
    for column in df.columns:
        ax.plot(df.index, df[column], label=column)
    
    ax.set_title(title, fontweight='bold')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.tick_params(axis='x', rotation=45)
    
    # Use custom formatter for y-axis
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(custom_formatter))
    
    if y_unit.startswith('Percentage'):
        ax.set_ylabel("Percentage (%)")
    else:
        ax.set_ylabel(y_unit)
    
    ax.autoscale(axis='y')

    # Format x-axis dates
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

def create_plot(start_date=None, end_date=None):
    try:
        plt.style.use('ggplot')
        fig, axs = plt.subplots(4, 2, figsize=(20, 40))
        fig.suptitle("Economic Data Visualization (FRED Data)", fontsize=24, fontweight='bold')

        categories = {
            "Inflation (Year-over-Year Change)": {
                "Food": "CPIUFDSL",
                "Shelter": "CUSR0000SAH1",
                "Transportation": "CUSR0000SAT1",
                "Energy": "CPIENGSL",
            },
            "Construction and Industrial Production (Year-over-Year Change)": {
                "Construction Spending": "TTLCONS",
                "Industrial Production": "INDPRO",
            },
            "Total Industry Capacity Utilization": {
                "Capacity Utilization": "TCU",
            },
            "Social Services Spending": {
                "Education": "G160291A027NBEA",
                "Health": "HLTHSCPCHCSA",
                "Social Benefits": "W823RC1",
            },
            "Financial Sector - Loans and Credit": {
                "Private Loans": "BUSLOANS",
                "Consumer Credit": "TOTALSL",
            },
            "Stock Market": {
                "S&P 500": "SP500",
            },
            "GDP Growth (Annual)": {
                "Real GDP": "A191RL1A225NBEA",
            },
            "Labor Market Indicators": {
                "Unemployment": "UNRATE",
                "Employment Population Ratio": "EMRATIO",
            }
        }

        y_units = {
            "Inflation (Year-over-Year Change)": "Percentage Change",
            "Construction and Industrial Production (Year-over-Year Change)": "Percentage Change",
            "Total Industry Capacity Utilization": "Percentage",
            "Social Services Spending": "Billions of Dollars",
            "Financial Sector - Loans and Credit": "Billions of Dollars",
            "Stock Market": "USD",
            "GDP Growth (Annual)": "Percentage Change",
            "Labor Market Indicators": "Percentage"
        }

        scales = {
            "Inflation (Year-over-Year Change)": "linear",
            "Construction and Industrial Production (Year-over-Year Change)": "linear",
            "Total Industry Capacity Utilization": "linear",
            "Social Services Spending": "log",
            "Financial Sector - Loans and Credit": "log",
            "Stock Market": "linear",
            "GDP Growth (Annual)": "linear",
            "Labor Market Indicators": "linear"
        }

        yoy_change = {
            "Inflation (Year-over-Year Change)": True,
            "Construction and Industrial Production (Year-over-Year Change)": True,
            "Total Industry Capacity Utilization": False,
            "Social Services Spending": False,
            "Financial Sector - Loans and Credit": False,
            "Stock Market": False,
            "GDP Growth (Annual)": False,
            "Labor Market Indicators": False
        }

        for i, (title, category) in enumerate(categories.items()):
            plot_section(axs[i//2, i%2], title, category, y_units[title], start_date, end_date, scale=scales[title], yoy_change=yoy_change[title])

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        return fig
    except Exception as e:
        st.error(f"Error creating plot: {str(e)}")
        return None

# Streamlit app
st.title("Economic Data Dashboard")
st.write("Real-time insights into key economic indicators")

st.write("Welcome to our Economic Data Dashboard. This tool provides a comprehensive overview of various economic indicators, helping you stay informed about the current state of the economy. The data is sourced from the Federal Reserve Economic Data (FRED) and is updated regularly.")

# Date range selection
date_range = st.radio("Select Date Range", ["Full History", "Last 10 Years"])

try:
    if date_range == "Full History":
        fig = create_plot()
    else:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365*10)
        st.write(f"Date range: {start_date.date()} to {end_date.date()}")  # Debug info
        fig = create_plot(start_date, end_date)

    if fig is not None:
        st.pyplot(fig)
    else:
        st.error("Unable to create plot. Please check the data and try again.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

# Add a refresh button
if st.button("Refresh Data"):
    st.rerun()
