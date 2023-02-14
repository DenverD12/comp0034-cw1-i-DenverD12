"""
Helper file with additional helper functions for basic tasks.

The first function loads the global dataframe.
The first function transposes the main dataframe and drops columns.
"""
from dash import html
import dash_bootstrap_components as dbc
from pathlib import Path
import pandas as pd


def load_dataframe():
    """
    Load prepared tourism arrivals dataframe from filepath.
    """
    # Global prepared dataset path for tourist arrivals
    TOURISM_DATA_FILEPATH = Path(__file__).parent.parent.joinpath(
        "tourism_hotels_app", "data", "Tourism_arrivals_prepared.csv"
    )
    # Import global prepared dataframe from above dataset
    df_arrivals_prepared = pd.read_csv(TOURISM_DATA_FILEPATH)
    return df_arrivals_prepared


def transpose_df_arrivals_prepared():
    """
    Transpose the prepared tourism arrivals dataframe and reset index to allow
    access to first column containing years.

    Args:
        None
    Returns:
        df_arrivals_transposed: Transposed pandas dataframe
    """
    df_arrivals_prepared = load_dataframe()
    # Drop all columns without numeric data, other than Country Name
    # Also drop average, minimum and maximum columns
    df_arrivals_prepared_drop = df_arrivals_prepared.drop(
        [
            "Region",
            "IncomeGroup",
            "Country Code",
            "Indicator Name",
            "10-year Average in tourist arrivals",
            "Max number of arrivals",
            "Minimum number of arrivals",
            "Percent drop 2019 to 2020",
        ],
        axis=1,
    )

    # Transpose dataframe and reset index to access first column for years
    df_arrivals_transposed = df_arrivals_prepared_drop.set_index(
        "Country Name"
    ).T.reset_index()
    return df_arrivals_transposed


def create_post_cards():
    """
    Create example post cards for the posts page (page 3).

    Args:
        None
    Returns:
        post_card_1, post_card_2, post_card_3: dbc cards with example posts
    """
    # Example empty image icon using copyright free link
    example_image_url = "http://www.example.com"

    # Create first example card
    post_card_1 = dbc.Card(
        dbc.CardBody(
            [
                html.H5(
                    "Example Hotel Name",
                    className="card-title d-flex justify-content-center",
                ),
                html.H6("Example Country and Location", className="card-subtitle"),
                html.Img(src=example_image_url),
                html.Br(),
                html.Br(),
                html.P(
                    "Example Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    className="card-text",
                ),
                html.P("5 Star Hotel", className="card-text"),
                html.P("Contact Email: email@gmail.com", className="card-text"),
            ]
        ),
        className="mb-3",
    )

    # Create second example card
    post_card_2 = dbc.Card(
        dbc.CardBody(
            [
                html.H5(
                    "Example Hotel Name",
                    className="card-title d-flex justify-content-center",
                ),
                html.H6("Example Country and Location", className="card-subtitle"),
                html.Img(src=example_image_url),
                html.Br(),
                html.Br(),
                html.P(
                    "Example Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    className="card-text",
                ),
                html.P("3 Star Hotel", className="card-text"),
                html.P("Contact Email: email@gmail.com", className="card-text"),
            ]
        ),
        className="mb-3",
    )

    # Create third example card
    post_card_3 = dbc.Card(
        dbc.CardBody(
            [
                html.H5(
                    "Example Hotel Name",
                    className="card-title d-flex justify-content-center",
                ),
                html.H6("Example Country and Location", className="card-subtitle"),
                html.Img(src=example_image_url),
                html.Br(),
                html.Br(),
                html.P(
                    "Example Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    className="card-text",
                ),
                html.P("4 Star Hotel", className="card-text"),
                html.P("Contact Email: email@gmail.com", className="card-text"),
            ]
        ),
        className="mb-3",
    )

    return post_card_1, post_card_2, post_card_3
