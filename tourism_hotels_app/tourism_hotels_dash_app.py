"""Main dash app."""
import dash
from dash import html, dcc, Dash, dash_table, Input, Output
import dash_bootstrap_components as dbc

# Create the dash app
app = Dash(__name__,
           # Use bootstrap css style sheet
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[
            # 
            {"name": "viewport", "content": "width=device-width, initial-scale=1"},
           ],
           use_pages=True
           )

# Wrap content of the dash app in a responsive width dbc container
app.layout = dbc.Container(
    # Set fluid to true to make container fill entire screen width
    fluid=True,
    children=[   
        # Blank line / line break
        html.Br(),

        # First row here
        ## Using dbc bootstrap to split page into rows and columns
        dbc.Row([
            dbc.Col(
                html.H1("Tourism"),
                width="auto")],
                justify="center",
                ),

        dbc.Row([
            dbc.Col(
                html.H2(
                     "International Tourist Arrivals",
                     className='lead'
                    ),
                width="auto")],
                justify="center",
                ),

        # Blank line / line break
        html.Br(),

        dash.page_container
            
    ],
    )

if __name__ == '__main__':
    app.run_server(debug=True)
