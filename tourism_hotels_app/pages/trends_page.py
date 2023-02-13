"""Contain the contents for the second page in multi-page app"""
import dash
from dash import html, dcc, Dash, Input, Output, State, callback
import dash_bootstrap_components as dbc
import create_charts as cc
import helper_functions as helper
import plotly.graph_objs as go


# Import global prepared dataframe from Tourism dataset
df_arrivals_prepared = helper.load_dataframe()

# Get list of country names from column
country_names_list = df_arrivals_prepared['Country Name'].unique()

dash.register_page(__name__)

layout = dbc.Container(
    fluid=True,
    children=[
        # First row here
        dbc.Row([
            dbc.Col([
                    ], 
                       
                width="auto")],
                justify="center",
                ),

        # Second row here for scatter plot for each country
        dbc.Row([
                # This is for the London area selector and the statistics panel
                dbc.Col([
                         html.Label(["Choose or type Country Name"]),
                         dcc.Dropdown(id='dropdown-scatter-per-country',
                                      options=[
                                              {'label': country,
                                               'value': country}
                                              for country in country_names_list
                                              ],
                                      # Set height between dropdown options
                                      optionHeight=35,
                                      value='Armenia',
                                      # Allow user to search available values
                                      searchable=True,
                                      # Default text shown if nothing selected
                                      placeholder='Please select...',
                                      # Prevemt user from clearing value
                                      clearable=False,
                                      style={'width': "100%"},
                                      # Allow last selected option to remain
                                      # if user refreshes browser tab
                                      persistence=True,
                                      persistence_type='session',
                                      ),
                         html.Br(),
                         html.Div(id="stats-card"),
                         ],
                        width=3,
                        # Increase vertical spacing to align with graph card
                        className="my-3",
                        # To reposition column position for smaller screen
                        ## For smallest screens make the columns on top of each other with max screen width
                        xs=12, sm=12, md=3, lg=3, xl=3
                        ),
                # Add the second column here. This is for the figure.
                dbc.Col([
                         # Add callback output title for scatter per country
                         html.H4(id='scatter-per-country-title'),
                         # Increased padding to stop corners of chart extruding the rounded corners
                         dbc.Card([
                            dcc.Graph(id='scatter-per-country'),
                                  ], className="p-1 px-2"
                                  ),
                        ],
                        width=9,
                        # To reposition column position for smaller screen
                        xs=12, sm=12, md=9, lg=9, xl=9
                        )
                ], justify="center"
                ),
            dbc.Row([
                dbc.Col([
                         html.H4(id='line-compare-countries-title'),
                         # Increased padding to stop corners of chart extruding the rounded corners
                         dbc.Card([
                            dcc.Graph(id='line-compare-countries'),
                                  ], className="p-1"
                                  ),

                    ],
                    width=8,
                    # To reposition column position for smaller screen
                    xs=12, sm=12, md=9, lg=8, xl=8
                    ),
                dbc.Col([
                         html.Label("Choose 2 countries to compare"),
                         dcc.Dropdown(id='dropdown-compare-countries-1',
                                      options=[
                                              {'label': country,
                                              'value': country}
                                              for country in country_names_list
                                              ],
                                      # Set height between dropdown options
                                      optionHeight=35,
                                      value='Bermuda',
                                      # Allow user to search available values
                                      searchable=True,
                                      # Default text shown if nothing selected
                                      placeholder='Select first country...',
                                      # Allow user to clear selected value
                                      clearable=False,
                                      style={'width': "100%"},
                                      # Allow last selected option to remain
                                      # if user refreshes browser tab
                                      persistence=True,
                                      persistence_type='session',
                                      ),
                        html.Br(),
                        dcc.Dropdown(id='dropdown-compare-countries-2',
                                      options=[
                                              {'label': country,
                                              'value': country}
                                              for country in country_names_list
                                              ],
                                      # Set height between dropdown options
                                      optionHeight=35,
                                      value='Bangladesh',
                                      # Allow user to search available values
                                      searchable=True,
                                      # Default text shown if nothing selected
                                      placeholder='Select second country...',
                                      # Allow user to clear selected value
                                      clearable=False,
                                      style={'width': "100%"},
                                      # Allow last selected option to remain
                                      # if user refreshes browser tab
                                      persistence=True,
                                      persistence_type='session',
                                      ),

                    ],
                    width=4,
                    # Increase vertical spacing to align with graph card
                    className="my-3",
                    # To reposition column position for smaller screen
                    xs=12, sm=12, md=3, lg=4, xl=4
                    ),
                
                ],justify="center"
                ),

                dbc.Row([
                         html.H5("Click to download the dataset as an Excel file", className="d-flex justify-content-center gy-3 fw-bold"),
                         dbc.Col([
                             dbc.Card([
                                 html.Button('Download data as Excel', 
                                              id="excel-download-button", n_clicks=0, 
                                              style={'background-color': 'lightgreen'}),
                                 dcc.Download(id="download-excel")
                                      ])
                                 ], width=6)
                               ], justify="center"),
                html.Br()

            ]),


@callback(
    [Output('line-compare-countries', 'figure'),
     Output('line-compare-countries-title', "children")],
    [Input('dropdown-compare-countries-1', 'value'),
     Input('dropdown-compare-countries-2', 'value')]
)
def updatate_compare_line_charts_and_title(country_name_1, country_name_2):

    fig_compare_countries_line = cc.create_line_chart_compare_countries(country_name_1, country_name_2)

    line_compare_chart_title = f'Comparison in tourist arrival trends between {country_name_1} and {country_name_2}'

    return fig_compare_countries_line, line_compare_chart_title


@callback(
    [Output("scatter-per-country", "figure"),
     Output("scatter-per-country-title", "children"),
     Output("stats-card", "children")
     ],
    [Input("dropdown-scatter-per-country", "value")]
)
def update_country_scatter_and_stats_card(country_name):

    # Call helper function to create scatter plot, given callback input
    fig_scatter_per_country = cc.create_scatter_per_country(country_name)

    # Set dataframe to the country name
    df_arrivals_reset_index = df_arrivals_prepared.set_index('Country Name')

    # Get minimum, maximum and 10-year average values per country
    average_10yr_per_country = \
        df_arrivals_reset_index.loc[
                                    country_name,
                                    '10-year Average in tourist arrivals'
                                    ]
    max_value_per_country = \
        df_arrivals_reset_index.loc[country_name,
                                    'Max number of arrivals'
                                    ]
    min_value_per_country = \
        df_arrivals_reset_index.loc[country_name,
                                    'Minimum number of arrivals'
                                    ]

    # Generate the bootstrap format card with statistics
    stats_card = dbc.Card(
        children=[
            dbc.CardBody(
                [
                    html.H4(
                        country_name, id="card-name", className="card-title fw-bolder text-dark"
                    ),
                    html.Br(),
                    html.H6("Average arrivals in last 10 years:", className="card-title text-primary"),
                    html.H4(average_10yr_per_country, className="card-text text-primary fw-bold"),
                    html.Br(),
                    html.H6("Peak no. of arrivals:",
                             className="card-title text-success",
                            ),
                    html.H4(
                        max_value_per_country, className="card-text text-success fw-bolder"
                    ),
                    html.Br(),
                    html.H6("Lowest no. of arrivals:", className="card-title text-danger"),
                    html.H4(min_value_per_country, className="card-text text-danger fw-bolder"),
                    html.Br(),
                ]
            )
        ],
    )

    return fig_scatter_per_country, f"Trends in tourist arrivals for {country_name}", stats_card



@callback(
    [Output("download-excel", "data")],
    [Input("excel-download-button", "n_clicks")],
    prevent_initial_call=True,
)
def download_raw_data(excel_clicks):

    # Set dataframe to the country name for cleaner download
    df_arrivals_reset_index = df_arrivals_prepared.set_index('Country Name')

    # If download button clicked, download data as excel
    excel_file_raw = dcc.send_data_frame(df_arrivals_reset_index.to_excel, "Tourism arrivals.xlsx", sheet_name="Main")

    return [excel_file_raw]


