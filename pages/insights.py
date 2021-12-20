# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc

# Imports from this application
from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Hypothesis Testing Market Fish Versus Wild Fish



            

            """
        ),
    ],
)

# ![pairplot](./assets/pairplot.png "pairplot")

layout = dbc.Row([column1])