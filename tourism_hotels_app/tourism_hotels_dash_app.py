"""Main dash app layout that links the multiple pages."""
import dash
from dash import html, dcc, Dash, Input, Output, State
import dash_bootstrap_components as dbc
from navbar import Navbar


# Create the dash app
app = Dash(
    __name__,
    # Use bootstrap css style sheet
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
    use_pages=True,
)

# Wrap content of the dash app in a responsive width dbc container
app.layout = dbc.Container(
    # Set fluid to true to make container fill entire screen width
    fluid=True,
    class_name="bg-light",
    children=[
        Navbar(),
        # Blank line / line break
        html.Br(),
        # First row here add the title
        dbc.Row(
            dbc.Col(
                [
                    html.H1(["International Tourism:"], className="text-dark"),
                ],
                width="auto",
            ),
            justify="center",
        ),
        # Second row add lead text
        dbc.Row(
            dbc.Col(
                html.H2(
                    ["Find the Best Destinations for Hospitality Development"],
                    className="lead text-dark",
                ),
                width="auto",
            ),
            justify="center",
        ),
        # Add line break
        html.Br(),
        # Add multi-page contents container
        dbc.Row(
            dbc.Col(
                dash.page_container,
            ),
            justify="center",
        ),
    ],
)


# add callback for toggling the search bar collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
