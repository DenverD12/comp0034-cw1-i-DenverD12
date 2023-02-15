"""Contain the contents for the first / home page in multi-page app"""
import dash
from dash import html, dcc, Dash, Input, Output, State, callback
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import create_charts as cc
import helper_functions as helper


# Import global prepared dataframe from Tourism dataset
df_arrivals_prepared = helper.load_dataframe()


dash.register_page(__name__, path="/")

# Wraps content of the dash app page in a responsive width dbc container
layout = dbc.Container(
    fluid=True,
    children=[
        # Use dbc to split page into rows and columns
        # First row here
        dbc.Row(
            [
                # Column containing options and pie chart
                dbc.Col(
                    [
                        html.Label(
                            ["Choose with arrows, or type a year between 1995 and 2020"]
                        ),
                        dbc.Row(
                            [
                                # Add input field to enter year as a number, numeric type
                                # Make field red if nothing entered or anything other than the specified type or range
                                dcc.Input(
                                    id="input_year_field",
                                    type="number",
                                    # Set debounce as true
                                    inputMode="numeric",
                                    debounce=True,
                                    # Set pre-selected value to 2019
                                    value=2019,
                                    # Set min and max to year range of available data columns
                                    max=2020,
                                    min=1995,
                                    step=1,
                                    required=True,
                                    # Increase padding, add rounded grey border
                                    className="p-1 rounded border border-secondary",
                                ),
                                # Add button to submit chosen year to update graphs only when it's clicked
                                html.Button(
                                    id="submit_button",
                                    n_clicks=0,
                                    children="Submit",
                                    className="my-1 rounded border-secondary",
                                ),
                                # Increase padding, horizontal gutter and change positioning for better visual appearance
                            ],
                            className="p-2 gx-3 my-0 py-0",
                        ),
                        dbc.Col(
                            [
                                html.Label(["Filter by Region"], className="text-dark"),
                                # Place region selector dropdown in card
                                dbc.Card(
                                    [
                                        dcc.Dropdown(
                                            id="region-dropdown",
                                            # Give options dictionary for each region and All regions
                                            options=[
                                                {
                                                    "label": "All regions",
                                                    "value": "All regions",
                                                },
                                                {
                                                    "label": "East Asia & Pacific",
                                                    "value": "East Asia & Pacific",
                                                },
                                                {
                                                    "label": "Europe & Central Asia",
                                                    "value": "Europe & Central Asia",
                                                },
                                                {
                                                    "label": "Latin America & Caribbean",
                                                    "value": "Latin America & Caribbean",
                                                },
                                                {
                                                    "label": "Middle East & North Africa",
                                                    "value": "Middle East & North Africa",
                                                },
                                                {
                                                    "label": "North America",
                                                    "value": "North America",
                                                },
                                                {
                                                    "label": "South Asia",
                                                    "value": "South Asia",
                                                },
                                                {
                                                    "label": "Sub-Saharan Africa",
                                                    "value": "Sub-Saharan Africa",
                                                },
                                            ],
                                            # Set height between dropdown options
                                            optionHeight=35,
                                            # Initially set to show all regions in pie and choropleth figure
                                            value="All regions",
                                            # Allow user to search available values
                                            searchable=True,
                                            # Default text shown if nothing selected
                                            placeholder="Please select...",
                                            # Allow user to clear selected value
                                            clearable=True,
                                            style={"width": "100%"},
                                            # Allow last selected option to remain if user refreshes browser tab
                                            persistence=True,
                                            persistence_type="session",
                                            className="border rounded",
                                        ),
                                    ],
                                    class_name="border border-white",
                                ),
                                # Add pie chart figure and title to be updated via callback
                                html.H5(id="pie-chart-title", className="my-3"),
                                dbc.Card(
                                    [
                                        dcc.Graph(id="pie-chart-regions"),
                                    ],
                                    # Center pie figure in card and change spacing and position
                                    className="py-0 p-1 my-0 gy-0 d-flex align-items-center justify-content-center",
                                ),
                            ],
                            className="my-2",
                        ),
                    ],
                    width=5,
                    className="my-2 p-2",
                    # Add column widths to reposition column position for smaller screens
                    xs=12,
                    sm=12,
                    md=12,
                    lg=12,
                    xl=5,
                ),
                dbc.Col(
                    [
                        # Add title of chart here, smaller than main dashboard title
                        html.H4(
                            [
                                "International Tourist Arrivals per Country by Year and Region"
                            ]
                        ),
                        # Add the choropleth figure in a card, updated via callback
                        dbc.Card(
                            [
                                dcc.Graph(id="choropleth"),
                            ],
                            # Align figure in centre of card and increase padding
                            class_name="d-flex align-items-center justify-content-center p-2 py-5",
                        ),
                    ],
                    width=7,
                    # Add column widths to reposition column position for smaller screens
                    xs=12,
                    sm=12,
                    md=12,
                    lg=12,
                    xl=7,
                ),
            ],
            justify="center",
        ),
        # Second Row Here
        dbc.Row(
            [
                dbc.Col(
                    [
                        # Add id for graph title output from callback
                        html.H4(id="bar-10yr-average-title", className="text-dark"),
                        dbc.Card(
                            [
                                html.Label(
                                    ["Choose between top 1 to top 15 countries"],
                                    className="text-dark",
                                ),
                                dcc.Slider(
                                    # Set slider options from 1 and 15 with initial value at 10
                                    min=1,
                                    max=15,
                                    step=1,
                                    value=10,
                                    # Add tooltip to make clear what year is selected
                                    tooltip={
                                        "placement": "bottom",
                                        "always_visible": True,
                                    },
                                    updatemode="mouseup",
                                    # Allow last slider selection to stay when browser refreshed for convenience
                                    persistence=True,
                                    persistence_type="session",
                                    id="top-x-slider",
                                ),
                            ],
                            class_name="p-2 my-2",
                        ),
                        dbc.Card(
                            [
                                dcc.Graph(
                                    # Create id to output bar figure using callback
                                    id="bar-10yr-average",
                                ),
                            ],
                            class_name="p-2",
                        ),
                    ]
                )
            ]
        ),
        html.Br(),
    ],
)


@callback(
    [
        Output("choropleth", "figure"),
        Output("pie-chart-regions", "figure"),
        Output("pie-chart-title", "children"),
    ],
    [Input("submit_button", "n_clicks"), Input("region-dropdown", "value")],
    [State("input_year_field", "value")],
)
def update_output(number_clicks, selected_region, year_selected):
    """
    Call back to update choropleth and pie figures, as well as the pie chart title when the year and/or region is changed

    :param number_clicks: Counts number of clicks of submit button, so state input for year is only updated when clicked
    :param selected_region: Value of selected region from region dropdown
    :param year_selected: Value of specific year chosen in input via typing or clicking arrows
    :return: Figure for choropleth and pie chart and pie chart title, filtered by year and region
    """

    # Prevent updates to chorpleth figure if no year selected
    if year_selected is None:
        raise PreventUpdate
    else:
        # Don't show all regions on one pie as it is too many colors
        if selected_region == "All regions":
            # Show middle east region instead
            fig_choropleth = cc.create_choropleth_map(year_selected, selected_region)
            fig_pie_chart_regions = cc.create_pie_chart(
                year_selected, "Middle East & North Africa"
            )
            pie_chart_title = f"Distribution of Arrivals in Middle East & North Africa in {year_selected}"
        else:
            # Run external helper function to create choropleth graph figure
            fig_choropleth = cc.create_choropleth_map(year_selected, selected_region)

            fig_pie_chart_regions = cc.create_pie_chart(year_selected, selected_region)

            pie_chart_title = (
                f"Distribution of Arrivals in {selected_region} in {year_selected}"
            )

        return fig_choropleth, fig_pie_chart_regions, pie_chart_title

    i


@callback(
    [
        Output("bar-10yr-average", "figure"),
        Output("bar-10yr-average-title", "children"),
    ],
    Input("top-x-slider", "value"),
)
def update_topx_tourism_graph(top_x_countries):
    """
    Call back for updating bar chart figure and title when slider value changed.

    :param top_x_countries: A number between 1 and 15 for top 1 to 15 countries
    :return: figure of plotly bar chart created in external file and title text that update depending on chosen value
    """
    fig_bar_chart_top_x_countries = cc.bar_chart_top_x_tourism_countries(
        top_x_countries
    )

    fig_bar_chart_title_text = (
        f"Top {top_x_countries} countries for international tourist arrivals"
    )

    return fig_bar_chart_top_x_countries, fig_bar_chart_title_text
