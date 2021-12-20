# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load, dump

# Imports from this application
from app import app

# Importing pickled model
model = load('./assets/model/TMWRandomForest.joblib')

# Creating sliders and dropdown for data input
gps_height_slider = html.Div(
    [
        dbc.Label("GPS Height", html_for="slider"),
        dcc.Slider(id="gps_height_slider", min=-63, max=2770, step=100, value=1237, tooltip={"placement": "bottom", "always_visible": True}),  
    ]
)

longitude_slider = html.Div(
    [
        dbc.Label("Longitude (Limited to boundaries of Tanzania)", html_for="slider"),
        dcc.Slider(id="longitude_slider", min=29.5, max=40.5, step=0.5, value=34.5, tooltip={"placement": "bottom", "always_visible": True}),  
    ]
)

latitude_slider = html.Div(
    [
        dbc.Label("Latitude (Limited to boundaries of Tanzania)", html_for="slider"),
        dcc.Slider(id="latitude_slider", min=-11.649440, max=-0.998464, step=0.5, value=-6.5, tooltip={"placement": "bottom", "always_visible": True}),  
    ]
)

quantity_dropdown = html.Div(
    [
        dbc.Label("Quantity of Water", html_for="dropdown"),
        dcc.Dropdown(
            id='quantity_dropdown',
            options=[
                {'label': 'dry', 'value': 0},
                {'label': 'enough', 'value': 1},
                {'label': 'insufficient', 'value': 2},
                {'label': 'seasonal', 'value': 3}
            ],
            value=1
        ),
    ]
)

years_in_service_slider = html.Div(
    [
        dbc.Label("Years in Service", html_for="slider"),
        dcc.Slider(id="years_in_service_slider", min=1, max=50, step=1, value=24, tooltip={"placement": "bottom", "always_visible": True}),
    ]
)

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Predictions

            This application allows you to predict the function status of waterpipes given information on GPS Height, Longitude, Latitude, Water Quantity, and Years in Service.
            The predictive model used for this application is a Random Forest Classifier. For this simplified demonstration, only the top five performing features are utilized.

            """
        ),
        
        gps_height_slider,
        longitude_slider,
        latitude_slider,
        quantity_dropdown,
        years_in_service_slider
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H1("Predicted Status of Waterpipe...", style={"text-align": "center", "color": "rgb(108,108,108)"}),
        html.H1(id="output", style={"text-align": "center", "color": "rgb(17,157,255)"}),

    ],
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('output', 'children'),
    [Input('gps_height_slider', 'value'),
     Input('longitude_slider', 'value'),
     Input('latitude_slider', 'value'),
     Input('quantity_dropdown', 'value'),
     Input('years_in_service_slider', 'value')],
)
def display_page(gps_height, longitude, latitude, quantity, years_in_service):

    data = [[gps_height, longitude, latitude, quantity, years_in_service]]

    # Predicts on user input
    output = model.predict(data)

    # Changing from numeric prediction to string
    pip_dic = {
        0: 'functional',
        1: 'functional needs repair',
        2: 'non functional'
    }
    return "{}".format(pip_dic[output[0]])
  
