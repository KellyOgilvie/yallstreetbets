# Y'all Street Bets

## Introduction

This repository contains multiple scripts designed to analyze and visualize stock data. Each script serves a specific purpose within the overall goal of providing insightful and actionable analytics for swing traders. This project is operated by the Y'all Street Bets investment club. We are not financial advisors. Use these scripts at your own risk. Read our license for more details.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Standalone Scripts](#standalone-scripts)
  - [Seasonal trend charting](#seasonal-trend-charting)
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

## Standalone scripts

### Seasonal trend charting

**Description:** This script fetches historical stock data and visualizes price trends.

**Usage:** Specify the stock ticker and the period of interest in the script variables.

**Example Commands:**
```bash
python script.py AAPL 5y monthly
```
```bash
python script.py AAPL 5y weekly
```

## Interface
### Overview
The Stock Analysis Interface is a web application built with Dash and Python, designed to provide users with financial analysis of stocks. The application allows users to input a stock ticker symbol, upon which it displays various financial metrics such as Beta, Expected Return, Book Value Per Share, and a trailing stop loss price calculated using the Average True Range (ATR).

### Features
- Stock Ticker Input: Enter any stock ticker to retrieve financial data and analysis.
- Real-time Analysis: Get up-to-date financial analysis including Beta, Expected Return, and Book Value Per Share based on the most recent data from Yahoo finance.
- Trailing Stop-Loss Target: Automatically calculates the best trailing stop loss price using ATR. The ATR provides a measure of an asset's volatility over a specified period, allowing traders to set stop losses based on actual market conditions rather than arbitrary fixed distances. This makes the ATR-based trailing stop loss particularly useful in volatile markets where price swings are significant.

ATR-Based Trailing Stop Loss Method:

Setting the Stop Loss: Determine a multiplier, commonly 1.5 to 3 times the ATR, depending on the desired tightness of the stop. The trailing stop loss is then set a fixed distance from the high price (for long positions) or low price (for short positions) based on this calculation.
Example: If the ATR is $5 and you choose a multiplier of 2 for a long position, your trailing stop loss will be set $10 below the highest price reached since entering the trade.
This method dynamically adjusts to reflect the asset’s typical price movements, providing a balanced approach that aims to minimize premature exits during normal market fluctuations while protecting profits from significant reversals. The ATR-based trailing stop loss is a popular choice among traders who wish to tailor their risk management strategies to better align with the volatility and price dynamics of the assets they are trading.


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
- Account for leap years in seasonality_charting.py
- Add industry analysis to seasonality_charting.py
- Allow user to switch between weekly and monthly via Plotly chart for seasonality_charting.py (requires creating a Dash app)
- Cyclical trend analysis
- Volatility clustering detection
- Intermarket analysis tool
- Sentiment analysis
- Earnings surprise momentum tracker
- Risk management
- Predictive modeling using machine learning
- Liquidity assessment tool
- Economic indicators

### Version 1.0.0 - 2024-04-16

#### Added
- `seasonality_charting.py`: Introduced a new script for analyzing and visualizing seasonal trends in stock prices.

### Version 1.1.0 - 2024-04-16

#### Added
- Added weekly analysis to seasonality_charting.py
- Accepts ticker and period as inputs when running the script in terminal for seasonality_charting.py


