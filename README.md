# Y'all Street Bets

## Introduction

This repository contains multiple scripts designed to analyze and visualize stock data. Each script serves a specific purpose within the overall goal of providing insightful and actionable analytics for swing traders. This project is operated by the Y'all Street Bets investment club. We are not financial advisors. Use these scripts at your own risk. Read our license for more details.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Standalone Scripts](#standalone-scripts)
  - [Seasonal trend charting](#seasonal-trend-charting)
  - [Backtest trailing stop-loss](#backtest-trsl)
- [Interface](#interface)
- [Contributing](#contributing)
- [Contact](#contact)
- [License and Disclaimer](#license-and-disclaimer)
- [Changelog](#changelog)

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Pip (Python package installer)

## Installation

Clone this repository to your local machine using:
```bash
git clone https://github.com/KellyOgilvie/yallstreetbets
```
Navigate to the repository directory and install required Python libraries:
```bash
pip install -r requirements.txt
```
To run the application, execute the following command from the root directory of your project:
```bash
python ysb_ui.py
```
After running the command, open your web browser and visit `http://localhost:8050` to view the app.

## Standalone scripts

### Seasonal trend charting

**Description:** This script fetches historical stock data and visualizes price trends.

**Usage:** Specify the stock ticker and the period of interest in the script variables.

**Example Commands:**
```bash
python seasonality_charting.py AAPL 5y monthly
```
```bash
python seasonality_charting.py AAPL 5y weekly
```

### Backtest trailing stop-loss

**Description:** 
This script provides a basic framework for backtesting the ATR-based trailing stop loss method. Adjust the parameters like num_trades, shares, atr_multiplier, and the date range for more tailored backtesting based on specific trading strategies or different market conditions.
**Implementation:**
The script initially calculates the ATR for each day across the entire dataset using a rolling window of 14 days. This means that for any given day \(t\), the ATR is calculated based on the previous 14 days, including day \(t\). When making a simulated purchase at a randomly selected day, it uses the ATR calculated at that point.

1. **ATR Calculation**:
   - The script calculates the True Range (TR) for each day using the highest of the following three values:
     - The difference between today's high and low (\( \text{High} - \text{Low} \)).
     - The absolute difference between today's high and the previous close (\( |\text{High} - \text{Previous Close}| \)).
     - The absolute difference between today's low and the previous close (\( |\text{Low} - \text{Previous Close}| \)).
   - It then calculates the ATR by taking a rolling average of the True Range over the last 14 days.

2. **Simulated Purchase**:
   - The script selects random dates from the historical data and simulates purchases on those dates.
   - For each simulated purchase, it starts checking each subsequent day to determine if the stock's price falls below the trailing stop loss level, which is calculated as:
     \[
     \text{Trailing Stop Loss} = \text{Peak Price since Purchase} - (\text{ATR at Current Day} \times \text{Multiplier})
     \]
   - The "Peak Price since Purchase" is updated daily if the current price is higher than the previous peak price.

3. **Using ATR from Purchase Day Onwards**:
   - The ATR used for the trailing stop calculation is from the day of purchase and every subsequent day until the position is exited. This means that if a purchase is made on day \( t \), the ATR from day \( t \) (which reflects the volatility of the previous 13 days plus day \( t \)) is used to calculate the initial trailing stop. For each following day, the updated ATR (reflecting its respective 14-day period) is used.

This approach ensures that the ATR used for the trailing stop calculations is dynamically updated to reflect recent market conditions, providing a realistic and practical application of volatility-based stop loss strategy.

## Interface
### Overview
The Stock Analysis Interface is a web application built with Dash and Python, designed to provide users with financial analysis of stocks. The application allows users to input a stock ticker symbol, upon which it displays various financial metrics such as Beta, Expected Return, Book Value Per Share, and a trailing stop loss price calculated using the Average True Range (ATR).

### Features
- Stock Ticker Input: Enter any stock ticker to retrieve financial data and analysis.
- Real-time Analysis: Get up-to-date financial analysis including Beta, Expected Return, and Book Value Per Share based on the most recent data from Yahoo finance.
- Trailing Stop-Loss Target: Automatically calculates the best trailing stop loss price using ATR. The ATR provides a measure of an asset's volatility over a specified period, allowing traders to set stop losses based on actual market conditions rather than arbitrary fixed distances. This makes the ATR-based trailing stop loss particularly useful in volatile markets where price swings are significant. This method dynamically adjusts to reflect the asset’s typical price movements, providing a balanced approach that aims to minimize premature exits during normal market fluctuations while protecting profits from significant reversals. The ATR-based trailing stop loss is a popular choice among traders who wish to tailor their risk management strategies to better align with the volatility and price dynamics of the assets they are trading.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Contact

For any inquiries or collaboration requests, please contact me at kellyeogilvie@gmail.com](mailto:kellyeogilvie@gmail.com).

## License and Disclaimer
This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0) - see the [LICENSE](LICENSE) file for details.

### Disclaimer
Please note that this application is provided on an "as is" basis and without warranties of any kind. Use it at your own risk. For more details, see the [LICENSE](LICENSE) file.
The creator of this project is not a financial advisor. By using this application, you acknowledge and agree that investments and trading involve significant risks and that you should consult a financial advisor before making any investment decisions.

## Changelog

All notable changes to this project will be documented in this section. The format is based on [Keep a Changelog](https://keepachangelog.com/).

### Unreleased
- Incorporate seasonality_charting.py into the Dash app
- Account for leap years in seasonality_charting.py
- Add industry analysis to seasonality_charting.py
- Allow user to switch between weekly and monthly via Plotly chart for seasonality_charting.py 
- Cyclical trend analysis
- Volatility clustering detection
- Intermarket analysis tool
- Sentiment analysis
- Earnings surprise momentum tracker
- Risk management
- Predictive modeling using machine learning
- Liquidity assessment tool
- Economic indicators
- Allow user to enter avg cost basis for trailing stop loss calculation

### Version 1.2.0 - 2024-04-23

#### Added
- Added a new Dash app for basic stock analysis
- Added a new function for calculating the best trailing stop loss price based on the last 14 days of volatility for that stock

### Version 1.1.0 - 2024-04-16

#### Added
- Added weekly analysis to seasonality_charting.py
- Accepts ticker and period as inputs when running the script in terminal for seasonality_charting.py

### Version 1.0.0 - 2024-04-16

#### Added
- `seasonality_charting.py`: Introduced a new script for analyzing and visualizing seasonal trends in stock prices.



