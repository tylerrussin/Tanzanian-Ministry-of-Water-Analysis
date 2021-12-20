# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, predictions, competition, process

navbar = dbc.NavbarSimple(
    brand='Tanzanian Ministry of Water Data Analysis',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('Competition', href='/competition', className='nav-link')), 
        dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')), 
    ],
    sticky='top',
    color='light', 
    light=True, 
    dark=False
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Tyler Russin', className='mr-2'), 
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:tylerrussin2@gmail.com', style={
                                                                                                                        "padding-top": "2px",
                                                                                                                        "padding-right": "2px",
                                                                                                                        "padding-bottom": "2px",
                                                                                                                        "padding-left": "10px",
                                                                                                                        "color": "rgb(17,157,255)"
                                                                                                                        }), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/Tyler9937/Tanzanian-Ministry-of-Water-Dataset-App', style={
                                                                                                                        "padding-top": "2px",
                                                                                                                        "padding-right": "2px",
                                                                                                                        "padding-bottom": "2px",
                                                                                                                        "padding-left": "2px",
                                                                                                                        "color": "rgb(17,157,255)"
                                                                                                                        }), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/tyler-russin/', style={
                                                                                                                        "padding-top": "2px",
                                                                                                                        "padding-right": "2px",
                                                                                                                        "padding-bottom": "2px",
                                                                                                                        "padding-left": "2px",
                                                                                                                        "color": "rgb(17,157,255)"
                                                                                                                        }), 
                ], 
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/competition':
        return competition.layout
    elif pathname == '/process':
        return process.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)