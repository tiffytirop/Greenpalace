
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

last_week_data = [
    {'date_field': '2023-08-01', 'is_sold': 10},
    {'date_field': '2023-08-02', 'is_sold': 15},
]

previous_week_data = [
    {'date_field': '2023-07-25', 'is_sold': 8},
    {'date_field': '2023-07-26', 'is_sold': 12},
]

# Convert the data to pandas DataFrame
df_last_week = pd.DataFrame(last_week_data)
df_previous_week = pd.DataFrame(previous_week_data)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(id='sales-chart')
])

# Define a callback to update the graph
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('sales-chart', 'clickData')] 
)
def update_graph(click_data):

    figure = {
        'data': [
            {
                'x': df_last_week['date_field'],
                'y': df_last_week['is_sold'],
                'type': 'bar',
                'name': 'Last Week'
            },
            {
                'x': df_previous_week['date_field'],
                'y': df_previous_week['is_sold'],
                'type': 'bar',
                'name': 'Previous Week'
            }
        ],
        'layout': {
            'title': 'Sales Comparison',
            'xaxis': {
                'title': 'Date'
            },
            'yaxis': {
                'title': 'Total Quantity Sold'
            }
        }
    }

    return figure
