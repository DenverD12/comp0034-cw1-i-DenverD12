"""Contain the contents for the second page in multi-page app"""
import dash
from dash import html, dcc, Dash, Input, Output, State, callback
import dash_bootstrap_components as dbc
import create_charts as cc
import helper_functions as helper
import plotly.graph_objs as go


# Import global prepared dataframe from Tourism dataset
df_arrivals_prepared = helper.load_dataframe()

# Get list of country names from corresponding column
country_names_list = df_arrivals_prepared["Country Name"].unique()

dash.register_page(__name__)

layout = (
    dbc.Container(
        fluid=True,
        children=[
            # First row here for line plot for one country
            dbc.Row(
                [
                    # Add the country selector and the statistics card
                    dbc.Col(
                        [
                            html.Label(["Choose or type Country Name"]),
                            dcc.Dropdown(
                                id="dropdown-line-per-country",
                                # Obtain country names from dataset as options
                                options=[
                                    {"label": country, "value": country}
                                    for country in country_names_list
                                ],
                                # Set height between dropdown options
                                optionHeight=35,
                                value="Armenia",
                                # Allow user to search available values
                                searchable=True,
                                # Default text shown if nothing selected
                                placeholder="Please select...",
                                # Prevent user from clearing value
                                clearable=False,
                                # Allow last selected option to remain if browser refresh
                                persistence=True,
                                persistence_type="session",
                            ),
                            html.Br(),
                            html.Div(id="stats-card"),
                        ],
                        width=3,
                        # Increase vertical spacing to align with graph card
                        className="my-3",
                        # Reposition column position for smaller screens like phones
                        # For smallest screens auto-move columns on top of each other with max screen width
                        xs=12,
                        sm=12,
                        md=3,
                        lg=3,
                        xl=3,
                    ),
                    # Second column for figure
                    dbc.Col(
                        [
                            # Add callback output title for line for one country
                            html.H4(id="line-per-country-title"),
                            # Increase padding to stop chart corners extruding rounded card corners
                            dbc.Card(
                                [
                                    dcc.Graph(id="line-per-country"),
                                ],
                                className="p-1 px-2",
                            ),
                        ],
                        width=9,
                        # Reposition column position for smaller screens
                        xs=12,
                        sm=12,
                        md=9,
                        lg=9,
                        xl=9,
                    ),
                ],
                justify="center",
            ),
            # New row for comparison line chart and options
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Label("Choose 2 countries to compare"),
                            dcc.Dropdown(
                                id="dropdown-compare-countries-1",
                                # Set dropdown options to be names of countries
                                options=[
                                    {"label": country, "value": country}
                                    for country in country_names_list
                                ],
                                # Set height between dropdown options
                                optionHeight=35,
                                value="Bermuda",
                                # Allow user to search available values
                                searchable=True,
                                # Default text shown if nothing selected
                                placeholder="Select first country...",
                                # Allow user to clear selected value
                                clearable=False,
                                style={"width": "100%"},
                                # Allow last selected option to remain if browser refresh
                                persistence=True,
                                persistence_type="session",
                            ),
                            html.Br(),
                            dcc.Dropdown(
                                id="dropdown-compare-countries-2",
                                options=[
                                    {"label": country, "value": country}
                                    for country in country_names_list
                                ],
                                optionHeight=35,
                                value="Bangladesh",
                                searchable=True,
                                placeholder="Select second country...",
                                clearable=False,
                                style={"width": "100%"},
                                persistence=True,
                                persistence_type="session",
                            ),
                        ],
                        width=3,
                        # Increase vertical spacing to align with graph card
                        className="my-3",
                        # Reposition column position for smaller screen
                        xs=12,
                        sm=12,
                        md=3,
                        lg=4,
                        xl=3,
                    ),
                    dbc.Col(
                        [
                            html.H4(id="line-compare-countries-title"),
                            # Increase padding to stop chart corners extruding rounded card corners
                            dbc.Card(
                                [
                                    dcc.Graph(id="line-compare-countries"),
                                ],
                                className="p-1",
                            ),
                        ],
                        width=9,
                        # Reposition column position for smaller screens
                        xs=12,
                        sm=12,
                        md=9,
                        lg=8,
                        xl=9,
                    ),
                ],
                justify="center",
            ),
            # Final row on page for download button
            dbc.Row(
                [
                    html.H5(
                        "Click to download the dataset as an Excel file",
                        className="d-flex justify-content-center gy-3 fw-bold",
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    # Add download button for user to download data as excel file in callback
                                    html.Button(
                                        "Download data as Excel",
                                        id="excel-download-button",
                                        n_clicks=0,
                                        style={"background-color": "lightgreen"},
                                    ),
                                    dcc.Download(id="download-excel"),
                                ]
                            )
                        ],
                        width=6,
                    ),
                ],
                justify="center",
            ),
            html.Br(),
        ],
    ),
)


@callback(
    [
        Output("line-per-country", "figure"),
        Output("line-per-country-title", "children"),
        Output("stats-card", "children"),
    ],
    [Input("dropdown-line-per-country", "value")],
)
def update_country_line_and_stats_card(country_name):
    """
    Callback to updates line plot figure and title per country value selected in dropwdown.
    """
    # Call helper function to create line plot, given callback input
    fig_line_per_country = cc.create_line_per_country(country_name)

    # Set dataframe to the country name
    df_arrivals_reset_index = df_arrivals_prepared.set_index("Country Name")

    # Get minimum, maximum and 10-year average values per country
    average_10yr_per_country = df_arrivals_reset_index.loc[
        country_name, "10-year Average in tourist arrivals"
    ]
    max_value_per_country = df_arrivals_reset_index.loc[
        country_name, "Max number of arrivals"
    ]
    min_value_per_country = df_arrivals_reset_index.loc[
        country_name, "Minimum number of arrivals"
    ]

    # Generate the bootstrap format card with statistics
    stats_card = dbc.Card(
        children=[
            dbc.CardHeader(
                [
                    html.H4(
                        country_name, id="card-name", className="fw-bold text-dark"
                    ),
                ],
                class_name="gx-1 p-3 py-2 m-0 bg-white",
            ),
            dbc.CardBody(
                [
                    # Add averages text and value as blue color
                    html.H6(
                        "Average arrivals in last 10 years:",
                        className="card-title text-primary",
                    ),
                    html.H4(
                        average_10yr_per_country,
                        className="card-text text-primary fw-bold",
                    ),
                    html.Br(),
                    # Add peak text and value as green colour and bold to stand out
                    html.H6(
                        "Peak no. of arrivals:",
                        className="card-title text-success",
                    ),
                    html.H4(
                        max_value_per_country,
                        className="card-text text-success fw-bolder",
                    ),
                    html.Br(),
                    # Add minium value text and value as red color and bold to stand out
                    html.H6(
                        "Lowest no. of arrivals:", className="card-title text-danger"
                    ),
                    html.H4(
                        min_value_per_country,
                        className="card-text text-danger fw-bolder",
                    ),
                    html.Br(),
                ],
                className="py-3",
            ),
        ],
    )

    return (
        fig_line_per_country,
        f"Trends in tourist arrivals for {country_name}",
        stats_card,
    )


@callback(
    [
        Output("line-compare-countries", "figure"),
        Output("line-compare-countries-title", "children"),
    ],
    [
        Input("dropdown-compare-countries-1", "value"),
        Input("dropdown-compare-countries-2", "value"),
    ],
)
def updatate_compare_line_charts_and_title(country_name_1, country_name_2):
    """
    Callback to update both country lines in comparison line chart, given 2 country names chosen in the dropdown.

    :param country_name_1: Name of first country selected in dropdown
    :param country_name_2: Name of second country selected in dropdown
    :return: Figure for line chart with both selected country lines and its updated title
    """
    # Use external helper function to create combined line chart
    fig_compare_countries_line = cc.create_line_chart_compare_countries(
        country_name_1, country_name_2
    )

    line_compare_chart_title = f"Comparison in tourist arrival trends between {country_name_1} and {country_name_2}"

    return fig_compare_countries_line, line_compare_chart_title


@callback(
    [Output("download-excel", "data")],
    [Input("excel-download-button", "n_clicks")],
    prevent_initial_call=True,
)
def download_raw_data(excel_clicks):
    """
    Callback to download raw data as excel file when download button clicked.

    :param country_name_1: number of clicks of the download button
    :return: raw excel file object to pass to the download dbc function and download file
    """
    # Set dataframe to the country name for cleaner download
    df_arrivals_reset_index = df_arrivals_prepared.set_index("Country Name")

    # If download button clicked, download data as excel
    excel_file_raw = dcc.send_data_frame(
        df_arrivals_reset_index.to_excel, "Tourism arrivals.xlsx", sheet_name="Main"
    )

    return [excel_file_raw]
