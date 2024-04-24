# Import required libraries
import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from stonks_fun import get_current_price, calculate_atr_stop_loss, analyze

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Input(id='input-ticker', type='text', placeholder='Enter stock ticker', debounce=True),
                dbc.Button('Analyze', id='button-analyze', color='primary', className='ms-2')
            ], width=4),
        ], className='my-3'),
        dbc.Row([
            dbc.Col([
                html.Div(id='output-analysis'),
                html.Div(id='output-atr')
            ])
        ])
    ])
])

# Callbacks to update the analysis and ATR stop loss
@app.callback(
    Output('output-analysis', 'children'),
    Output('output-atr', 'children'),
    Input('button-analyze', 'n_clicks'),
    State('input-ticker', 'value')
)
def update_output(n_clicks, ticker):
    if n_clicks is None or ticker is None:
        return "", ""
    try:
        results = analyze(ticker)
        analysis_text = html.Div([
            html.H5(f"Analysis Results for {ticker}:"),
            html.P(f"Beta: {results['Beta']}"),
            html.P(f"Expected Return: {results['Expected Return']}"),
            html.P(f"Book Value Per Share: {results['Book Value Per Share']}")
        ])

        trailing_stop_loss = calculate_atr_stop_loss(ticker)
        atr_text = html.Div([
            html.H5("Trailing Stop Loss:"),
            html.P(f"{trailing_stop_loss:.2f}")
        ])

        return analysis_text, atr_text
    except Exception as e:
        return f"Error: {str(e)}", ""

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
