import yfinance as yf
import plotly.express as px
import plotly.graph_objs as go

ticker = 'AAPL'
years_back = '5y'

# Fetch historical data for the given ticker for the specified period
stock_data = yf.download(ticker, period=years_back)

# Extract year and month from the index
stock_data['Year'] = stock_data.index.year
stock_data['Month'] = stock_data.index.month

# Group the data by Year and Month, then calculate average monthly close price
monthly_data = stock_data.groupby(['Year', 'Month']).agg({'Close': 'mean'}).reset_index()

# Calculate the yearly average close price
yearly_avg = monthly_data.groupby('Year')['Close'].transform('mean')

# Calculate percentage from the yearly average and normalize
monthly_data['Normalized Close'] = (monthly_data['Close'] - yearly_avg) / yearly_avg * 100

# Pivot the data for plotting
pivot_data = monthly_data.pivot(index='Month', columns='Year', values='Normalized Close')

# Create a line plot using Plotly
fig = px.line(pivot_data, x=pivot_data.index, y=pivot_data.columns,
              labels={'value': 'Percent from Yearly Average', 'index': 'Month'},
              title=f'Normalized Seasonal Trends in {ticker} Stock Prices')

# Calculate the average across all years for each month
average_trend = pivot_data.mean(axis=1)

# Add the average trendline
fig.add_trace(go.Scatter(x=pivot_data.index, y=average_trend, mode='lines',
                         line=dict(color='black', width=3),
                         name='Average Trend'))

fig.update_xaxes(dtick="M1", tickformat="%b")
fig.show()
