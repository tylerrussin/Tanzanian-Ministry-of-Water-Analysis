import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from app import app

# Component to display markdown on left of screen
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Looking into Classification

            This web application demonstrates the classification of Tanzanian water pipes through the use of a Random Forest Classification model. To create the predictive model an in-depth data analysis, hyperparameter tuning, and a model analysis including feature importances, precision/recall, and ROC AUC scores were conducted. The model performs with an accuracy score of 80 percent.

            """
        ),
        dcc.Link(dbc.Button('View Model', color='primary'), href='/predictions')
    ],
    md=4,
)

# Creating the Longitude/Latitude scatter plot
y = pd.read_csv('./assets/data/dependent_vars.csv')
X = pd.read_csv('./assets/data/independent_vars.csv')
df = X.merge(y, on='id')
df = df[df['longitude'] > 10]
fig = px.scatter(df, x='longitude', y='latitude', color='status_group')

# Component to display scatter plot
column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

# Returns layout to be rendered on web page
layout = dbc.Row([column1, column2])