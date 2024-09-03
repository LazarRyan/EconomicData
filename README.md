# EconomicData

# Economic Data Dashboard

## Overview

The Economic Data Dashboard is an interactive web application that provides real-time insights into key economic indicators. Built with Python and Streamlit, this dashboard fetches data from the Federal Reserve Economic Data (FRED) API and presents it through intuitive visualizations.

## Features

- Real-time data fetching from FRED API
- Interactive visualizations of multiple economic indicators:
  - Inflation (Year-over-Year Change)
  - Construction and Industrial Production
  - Total Industry Capacity Utilization
  - Social Services Spending
  - Financial Sector - Loans and Credit
  - Stock Market Performance
  - GDP Growth (Annual)
  - Labor Market Indicators
- Customizable date range selection
- Responsive design for various screen sizes

## Technologies Used

- Python 3.x
- Streamlit
- Matplotlib
- Pandas
- FRED API
- NumPy

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/economic-data-dashboard.git
   cd economic-data-dashboard
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your FRED API key:
   - Sign up for a FRED API key at https://fred.stlouisfed.org/docs/api/api_key.html
   - Create a `.streamlit/secrets.toml` file in the project directory
   - Add your API key to the file:
     ```
     FRED_API_KEY = "your_api_key_here"
     ```

## Usage

Run the Streamlit app:

streamlit run streamlit_app.py

## Project Structure

- `streamlit_app.py`: Main application file containing the Streamlit app and data visualization logic
- `requirements.txt`: List of Python dependencies
- `.streamlit/secrets.toml`: Configuration file for storing the FRED API key (not included in repository)

## Data Sources

All economic data is sourced from the Federal Reserve Economic Data (FRED) database. The specific series used are:

- CPIUFDSL: Food Inflation
- CUSR0000SAH1: Shelter Inflation
- CUSR0000SAT1: Transportation Inflation
- CPIENGSL: Energy Inflation
- TTLCONS: Construction Spending
- INDPRO: Industrial Production
- TCU: Total Industry Capacity Utilization
- G160291A027NBEA: Education Spending
- HLTHSCPCHCSA: Health Spending
- W823RC1: Social Benefits
- BUSLOANS: Private Loans
- TOTALSL: Consumer Credit
- SP500: S&P 500 Index
- A191RL1A225NBEA: Real GDP Growth
- UNRATE: Unemployment Rate
- EMRATIO: Employment Population Ratio

## Contributing

Contributions to improve the dashboard are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Ryan Lazar - [lazar.ryan123@gmail.com](mailto:lazar.ryan123@gmail.com)

Project Link: [https://github.com/LazarRyan/economic-data-dashboard](https://github.com/LazarRyan/economic-data-dashboard)
