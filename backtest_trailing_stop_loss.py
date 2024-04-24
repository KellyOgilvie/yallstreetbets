import yfinance as yf
import pandas as pd
import numpy as np


def calculate_atr(data, period=14):
    data['High-Low'] = data['High'] - data['Low']
    data['High-Close'] = abs(data['High'] - data['Close'].shift())
    data['Low-Close'] = abs(data['Low'] - data['Close'].shift())
    data['TR'] = data[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
    data['ATR'] = data['TR'].rolling(window=period).mean()
    return data

def simulate_trades(data, num_trades=10, shares=100, atr_multiplier=2):
    # Ensure the DataFrame index is numerical for range operations
    data = data.reset_index(drop=True)
    purchase_indices = np.random.choice(data.index[num_trades:-1], size=num_trades, replace=False)
    results = []

    for index in purchase_indices:
        entry_price = data.loc[index, 'Close']
        peak_price = entry_price
        cost_basis = entry_price * shares
        exit_price = None

        # Adjusted to use numerical indices
        for j in range(index, len(data)):
            current_price = data.loc[j, 'Close']
            peak_price = max(peak_price, current_price)
            stop_loss = peak_price - atr_multiplier * data.loc[j, 'ATR']

            if current_price <= stop_loss:
                exit_price = current_price
                break

        if exit_price is None:
            exit_price = data['Close'].iloc[-1]

        exit_value = exit_price * shares
        profit_loss = exit_value - cost_basis
        profit_loss_percentage = (profit_loss / cost_basis) * 100
        results.append((cost_basis, exit_value, profit_loss, profit_loss_percentage))

    return results



# List of tickers to backtest
tickers = ['TSLA', 'RIVN', 'CHWY', 'AAPL']
backtest_results = {}

for ticker in tickers:
    data = yf.download(ticker, start="2019-01-01", end="2023-01-01")
    data = calculate_atr(data)
    results = simulate_trades(data)
    backtest_results[ticker] = results
    total_profit_loss = sum(result[2] for result in results)
    total_profit_loss_percentage = sum(result[3] for result in results)
    print(f"{ticker} - Total Profit/Loss: ${total_profit_loss:.2f}, Percentage: {total_profit_loss_percentage:.2f}%")

# To see detailed results per trade
print(backtest_results)
