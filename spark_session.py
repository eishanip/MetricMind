from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import dash
from dash import dcc, html
import plotly.express as px

# Initialize SparkSession
spark = SparkSession.builder.appName("KPI Dashboard").getOrCreate()

# Create a Dataset with countries
data = [
    ('USA', 'Jan', 12000, 100, 80), ('USA', 'Feb', 15000, 200, 70),
    ('USA', 'Mar', 10000, 150, 65),
    ('Canada', 'Jan', 11000, 95, 60), ('Canada', 'Feb', 14000, 185, 72),
    ('Canada', 'Mar', 10500, 175, 67),
    ('France', 'Jan', 13000, 110, 85), ('France', 'Feb', 15500, 205, 77),
    ('France', 'Mar', 12000, 190, 75),
    ('Germany', 'Jan', 12500, 105, 80), ('Germany', 'Feb', 16000, 210, 68),
    ('Germany', 'Mar', 11500, 165, 70),
    ('Mexico', 'Jan', 9000, 80, 60), ('Mexico', 'Feb', 12000, 150, 65),
    ('Mexico', 'Mar', 9500, 130, 60),
]

# Create a Spark DataFrame with new data (including country)
columns = ['Country', 'Month', 'Sales', 'CustomerEngagement', 'InventoryLevels']
df_spark = spark.createDataFrame(data, schema=columns)

# Data processing using Spark (example: filtering)
df_filtered = df_spark.filter(col('Sales') > 10000)

# Collecting data back to Python for visualization
data_for_dash = df_filtered.toPandas()

# Dash app initialization for visualization
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Big Data KPI Dashboard for Multiple Countries (Hadoop & Spark)"),
    dcc.Tabs([
        dcc.Tab(label="Sales Trends", children=[
            dcc.Graph(
                id='sales-trend-graph',
                figure=px.line(
                    data_for_dash, x='Month', y='Sales',
                    color='Country', title='Monthly Sales Trends by Country'
                )
            )
        ]),
        dcc.Tab(label="Customer Engagement", children=[
            dcc.Graph(
                id='customer-engagement-graph',
                figure=px.bar(
                    data_for_dash, x='Month', y='CustomerEngagement',
                    color='Country', title='Customer Engagement by Country'
                )
            )
        ]),
        dcc.Tab(label="Inventory Levels", children=[
            dcc.Graph(
                id='inventory-levels-graph',
                figure=px.line(
                    data_for_dash, x='Month', y='InventoryLevels',
                    color='Country', title='Inventory Levels by Country'
                )
            )
        ])
    ])
])

# Running the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
