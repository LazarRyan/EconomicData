# EconomicData

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

Your Name - [lazar.ryan123@gmail.com](mailto:lazar.ryan123@gmail.com)

Project Link: [https://github.com/LazarRyan/economic-data-dashboard](https://github.com/LazarRyan/economic-data-dashboard)
