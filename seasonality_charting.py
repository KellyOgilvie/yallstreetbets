import sys
import yfinance as yf
import plotly.express as px
import plotly.graph_objs as go

# Set default values
default_ticker = 'AAPL'
default_period = '5y'
default_frequency = 'monthly'  # Or 'weekly'

# Read command line arguments and assign defaults if not provided
if len(sys.argv) > 1:
    ticker = sys.argv[1]
else:
    ticker = default_ticker

if len(sys.argv) > 2:
    years_back = sys.argv[2]
else:
    years_back = default_period

if len(sys.argv) > 3:
    frequency = sys.argv[3]
else:
    frequency = default_frequency

# Fetch historical data for the given ticker for the specified period
stock_data = yf.download(ticker, period=years_back)

# Extract year and month from the index
stock_data['Year'] = stock_data.index.year
stock_data['Month'] = stock_data.index.month
stock_data['Week'] = stock_data.index.isocalendar().week

# Group the data by Year and Month or Week, then calculate average close price
if frequency == 'monthly':
    group_data = stock_data.groupby(['Year', 'Month']).agg({'Close': 'mean'}).reset_index()
    time_unit = 'Month'
elif frequency == 'weekly':
    group_data = stock_data.groupby(['Year', 'Week']).agg({'Close': 'mean'}).reset_index()
    time_unit = 'Week'

# Calculate the yearly average close price
yearly_avg = group_data.groupby('Year')['Close'].transform('mean')

# Calculate percentage from the yearly average and normalize
group_data['Normalized Close'] = (group_data['Close'] - yearly_avg) / yearly_avg * 100

# Pivot the data for plotting
pivot_data = group_data.pivot(index=time_unit, columns='Year', values='Normalized Close')

# Create a line plot using Plotly
fig = px.line(pivot_data, x=pivot_data.index, y=pivot_data.columns,
              labels={'value': 'Percent from Yearly Average', 'index': time_unit},
              title=f'Normalized Seasonal Trends in {ticker} Stock Prices ({frequency.capitalize()})')

# Calculate the average across all years for each month or week
average_trend = pivot_data.mean(axis=1)

# Add the average trendline
fig.add_trace(go.Scatter(x=pivot_data.index, y=average_trend, mode='lines',
                         line=dict(color='black', width=3),
                         name='Average Trend'))

fig.update_xaxes(dtick="M1" if frequency == 'monthly' else "W1", tickformat="%b" if frequency == 'monthly' else None)
fig.show()
