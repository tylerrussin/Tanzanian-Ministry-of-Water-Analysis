import dash
import dash_bootstrap_components as dbc


external_stylesheets = [
    dbc.themes.BOOTSTRAP,                                          # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css',     # For social media icons
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

# Creating dash app with external stylesheets and meta tags
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True                      # Supressing url callback expressions
app.title = 'Tanzanian Ministry of Water Data Analysis'             # Browser title bar
server = app.server                                                 # Setting app server