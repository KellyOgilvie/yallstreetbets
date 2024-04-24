from yahoo_fin import stock_info
import yfinance as yf
yf.pdr_override()  # fixes bug with datareader

import pandas as pd
from pandas import *
from pandas_datareader.data import DataReader
from datetime import date

def calculate_atr_stop_loss(ticker, period=14, multiplier=1.5):
    """
    Calculate the trailing stop loss for a stock using the Average True Range (ATR).

    Parameters:
        ticker (str): Stock ticker symbol.
        period (int): Number of days to calculate the ATR over.
        multiplier (float): Multiplier for the ATR to set the stop loss distance.

    Returns:
        float: Trailing stop loss price.
    """
    # Fetch historical data
    data = yf.download(ticker, period=f'{period * 2}d')

    # Calculate the true range (TR)
    data['High-Low'] = data['High'] - data['Low']
    data['High-Close'] = abs(data['High'] - data['Adj Close'].shift())
    data['Low-Close'] = abs(data['Low'] - data['Adj Close'].shift())
    data['TR'] = data[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)

    # Calculate the ATR
    data['ATR'] = data['TR'].rolling(window=period).mean()

    # Most recent closing price
    latest_close = data['Adj Close'].iloc[-1]

    # Calculate trailing stop loss price
    trailing_stop_loss = latest_close - (data['ATR'].iloc[-1] * multiplier)

    return trailing_stop_loss



def get_current_price(ticker):
    """
    Fetch the current price of the stock.
    input: stock ticker (str)
    output: price (str) or error message (str)
    """
    try:
        # Get current price of the ticker
        price = stock_info.get_live_price(ticker)
        return price

    except Exception as e:
        # If there's an error (e.g., invalid stock ticker), display it
        return f"Error: {e}"


def calculate_return(data):
    """
    Calculate the return over a period.
    Return = today's adj closing - yesterday's adj closing
    input: dataframe with column for Adj Close
    output: column of return values
    """
    return data['Adj Close'].pct_change() * 100


def get_data(ticker, start=date(2024, 1, 1), end=date(2024, 3, 15), interval="daily"):
    """
    Get stock data from Yahoo finance
    input: ticker (str), start date (date), end date (date), interval= daily, weekly, monthly (str)
    output: dataframe
    """
    try:
        # Get data for the specified period
        data = DataReader(ticker, start=start, end=end)
        return data

    except Exception as e:
        # If there's an error (e.g., invalid stock ticker), return that instead
        print(f"Error: {e}")
        return f"Error: {e}"


def analyze(ticker, market_ticker='SPY', start=date(2024, 1, 1), end=date(2024, 3, 15), interval="daily"):
    """
    Stonk Analyzer analyzes stonks.
    input: ticker (str), start date (date), end date (date), interval= daily, weekly, monthly (str)
    TODO: interval doesn't do anything yet
    """
    # Get metadata for the stock
    stock = yf.Ticker(ticker)

    # Collect full stock data for the time period
    stock_data = get_data(ticker, start, end)
    market_data = get_data(market_ticker, start, end)

    # Calculate the returns
    stock_returns = calculate_return(stock_data)
    market_returns = calculate_return(market_data)

    # Calculate Beta
    #covariance = stock_returns.cov(market_returns)
    #variance = market_returns.var()
    #beta = covariance/variance

    # Get the Beta
    beta = stock.info['beta']
    # Get the book value per share
    bvps = stock.info['bookValue']

    # Calculate Expected Return of the stock using CAPM
    risk_free_rate = 4.25 # TODO: actually get the current real rfr
    expected_market_return = 8.00 # TODO: actually calculate this
    capm = risk_free_rate + beta * (expected_market_return - risk_free_rate)

    results = {
        "Beta": beta,
        "Expected Return": capm,
        "Book Value Per Share": bvps
    }

    return(results)


