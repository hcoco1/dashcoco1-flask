# dash_app/index.py
from dash import Dash
import dash_bootstrap_components as dbc
from dash_app.components.layout import create_layout
from dash_app.components.callbacks import register_callbacks

def create_dash_app(flask_app, df):
    dash_app = Dash(
        server=flask_app,
        routes_pathname_prefix='/dash/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    # Set the layout for the Dash app
    dash_app.layout = create_layout(df)

    # Register callbacks
    register_callbacks(dash_app, df)

    return dash_app



