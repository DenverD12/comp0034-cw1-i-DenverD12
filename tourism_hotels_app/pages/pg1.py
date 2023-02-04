import dash
from dash import html, dcc, Dash, dash_table, Input, Output
import dash_bootstrap_components as dbc
import pages.create_charts as cc
import plotly.express as px


dash.register_page(__name__, path='/')

# Wraps content of the dash app page in a responsive width dbc container
layout = dbc.Container(
    fluid=True,
    children=[
        # First row here
        ## Using dbc bootstrap to split page into rows and columns
        dbc.Row([
            dbc.Col(
                html.H1("Tourism"),
                width="auto")],
                justify="center",
                ),
        ]
)
