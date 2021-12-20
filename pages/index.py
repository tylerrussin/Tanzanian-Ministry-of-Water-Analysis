# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Looking into Classification

            In this web application, we explore the key concepts of Data Wrangling and Classification. Scoring metrics such as Precision/Recall and ROC AUC scores are utilized. Pipeline building techniques associated with Data Preprocessing, Hyperparameter Tuning, and Cross-Validation are implemented.

            This application describes the competition that was entered, the process for  how modeling was done, and has an interactive model demo

            """
        ),
        dcc.Link(dbc.Button('View Model', color='primary'), href='/predictions')
    ],
    md=4,
)
import plotly.express as px
y = pd.read_csv('./assets/data/dependent_vars.csv')
X = pd.read_csv('./assets/data/independent_vars.csv')
df = X.merge(y, on='id')
df = df[df['longitude'] > 10]
fig = px.scatter(df, x='longitude', y='latitude', color='status_group')


column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])