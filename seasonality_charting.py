import sys
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

# Define industry tickers
industry_tickers = ['BA', 'AAL', 'UAL']  # Example for tech industry
default_period = '3y'

# Read command line arguments and assign defaults if not provided
years_back = sys.argv[1] if len(sys.argv) > 1 else default_period

# Create an empty figure for the plots
fig = go.Figure()

# Dataframe to store all normalized closes for trend line calculation
all_normalized_closes = pd.DataFrame()

# Fetch and process historical data for each ticker in the industry
for ticker in industry_tickers:
    stock_data = yf.download(ticker, period=years_back)
    stock_data['Year'] = stock_data.index.year
    stock_data['Month'] = stock_data.index.month

    # Group data and calculate mean close prices
    grouped_data = stock_data.groupby(['Year', 'Month']).agg({'Close': 'mean'}).reset_index()

    # Calculate the yearly average close price
    yearly_avg = grouped_data.groupby('Year')['Close'].transform('mean')

    # Calculate percentage from the yearly average and normalize
    grouped_data['Normalized Close'] = (grouped_data['Close'] - yearly_avg) / yearly_avg * 100
    all_normalized_closes = pd.concat([all_normalized_closes, grouped_data[['Normalized Close', 'Month']]], axis=0)

    # Pivot data for plotting
    pivot_data = grouped_data.pivot(index='Month', columns='Year', values='Normalized Close')

    # Add a trace for each year for this ticker
    for year in pivot_data.columns:
        fig.add_trace(go.Scatter(x=pivot_data.index, y=pivot_data[year], mode='lines', name=f'{ticker} {year}', line=dict(color='black')))

# Calculate and plot the average trendline across all normalized closes
avg_trendline = all_normalized_closes.groupby('Month')['Normalized Close'].mean()
fig.add_trace(go.Scatter(x=avg_trendline.index, y=avg_trendline, mode='lines', name='Average Trend', line=dict(color='red', width=3)))

# Update layout and axes properties
fig.update_layout(title='Normalized Seasonal Trends in Industry Stock Prices (Monthly)',
                  xaxis_title='Month',
                  yaxis_title='Percent from Yearly Average',
                  legend_title="Ticker and Year")

fig.update_xaxes(dtick="M1", tickformat="%b")

# Show the plot
fig.show()
