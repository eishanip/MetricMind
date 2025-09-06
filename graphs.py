from dash import dcc, html
import dash
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Country': ['USA', 'Canada', 'France', 'Germany', 'Mexico'],
    'Sales': [25000, 15000, 12000, 22000, 10000],
    'Customer_Engagement': [80, 60, 70, 90, 50],
    'Inventory_Levels': [500, 300, 200, 400, 150]
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Bar Chart - Sales by Country
bar_fig = px.bar(
    df, x='Country', y='Sales', title='Sales by Country',
    color='Country',
    labels={'Sales': 'Total Sales (in USD)', 'Country': 'Country'},
    text='Sales'
)

# Pie Chart - Market Share of Sales
pie_fig = px.pie(
    df, names='Country', values='Sales', title='Market Share of Sales',
    labels={'Country': 'Country', 'Sales': 'Sales'}
)

# Scatter Plot - Customer Engagement vs Sales
scatter_fig = px.scatter(
    df, x='Sales', y='Customer_Engagement',
    color='Country', size='Inventory_Levels',
    title='Customer Engagement vs Sales',
    labels={'Sales': 'Sales (in USD)', 'Customer_Engagement': 'Customer Engagement (%)'}
)

# Line Graph - Sales and Inventory Levels by Country
line_fig = px.line(
    df, x='Country', y=['Sales', 'Inventory_Levels'],
    title='Sales and Inventory Levels by Country',
    labels={'value': 'Values', 'variable': 'Metric', 'Country': 'Country'}
)

# Layout for Dash App with Tabs
app.layout = html.Div([
    html.H1("Dashboard for KPI Monitoring", style={'textAlign': 'center'}),

    dcc.Tabs([
        dcc.Tab(label="Sales by Country", children=[
            dcc.Graph(id='bar-graph', figure=bar_fig)
        ]),

        dcc.Tab(label="Market Share of Sales", children=[
            dcc.Graph(id='pie-chart', figure=pie_fig)
        ]),

        dcc.Tab(label="Customer Engagement vs Sales", children=[
            dcc.Graph(id='scatter-plot', figure=scatter_fig)
        ]),

        dcc.Tab(label="Sales & Inventory Levels", children=[
            dcc.Graph(id='line-graph', figure=line_fig)
        ])
    ])
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
