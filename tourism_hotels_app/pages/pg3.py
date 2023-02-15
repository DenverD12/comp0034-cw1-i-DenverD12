"""Contain the contents for the third page in multi-page app"""
import dash
from dash import html, dcc, Dash, Input, Output, State, callback
import dash_bootstrap_components as dbc
import helper_functions as helper

dash.register_page(__name__)

# Create 3 dbc cards with example locations posted using helper function
post_card_1, pst_card_2, post_card_3 = helper.create_post_cards()


layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            [
                # Add title and lead title for posts page with text centered
                html.H4(
                    ["Existing or Planned Hospitality Location Posts"],
                    id="card-name",
                    className="card-title text-dark d-flex justify-content-center",
                ),
                html.H5(
                    [
                        "Post your location and details to collaborate with others in the hospitality sector!"
                    ],
                    className="d-flex justify-content-center lead",
                ),
                html.Br(),
                html.Br(),
                # Example existing (already posted) locations
                # Auto-update width and position when screen size decreased.
                dbc.Col([post_card_1], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                dbc.Col([pst_card_2], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                dbc.Col([post_card_3], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                dbc.Col([post_card_1], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                dbc.Col([pst_card_2], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                # Have empty div to hold any new locations posted by user
                dbc.Col(
                    html.Div(id="added-posts-container"),
                    width=4,
                    xs=12,
                    sm=12,
                    md=6,
                    lg=4,
                    xl=4,
                ),
            ],
            justify="center",
        ),
        # Add blue informative text
        html.H5(
            ["Have your own location to add? Login to post your own!"],
            className="text-primary fw-bold d-flex justify-content-center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        # Add login button connected to callback with id
                        html.Button(
                            ["Login to post"],
                            id="login-unhide-button",
                            n_clicks=0,
                            className="bg-info p-2 border rounded border-secondary",
                        ),
                    ],
                    width="auto",
                )
            ],
            justify="center",
        ),
        dbc.Row(
            [
                # Add empty containers for login and output to be unhidden upon callback
                dbc.Col(
                    [
                        html.Div(id="login-container"),
                        html.Div(id="create-posts-container"),
                    ],
                    width="auto",
                )
            ],
            justify="center",
        ),
    ],
)


@callback(
    [Output("login-container", "children")],
    [Input("login-unhide-button", "n_clicks")],
    suppress_callback_exceptions=True,
)
def unhide_login_fields(n_clicks_login_unhide):
    """
    Callback to unhide the login fields after user clicks "login-unhide-button'.

    :param n_clicks_login_unhide: Number of clicks of the "login-unhide-button"
    :return: dbc card with login input components displayed in empty div in main layout
    """
    # If button clicked an odd number of times, unhide login container
    if n_clicks_login_unhide:
        login_card = dbc.Container(
            children=[
                dbc.CardBody(
                    [
                        # Add input fields for username and password
                        dcc.Input(
                            id="input", placeholder="Enter Username", type="text"
                        ),
                        dcc.Input(
                            id="password", placeholder="Enter Password", type="password"
                        ),
                        # Add button to submit inputted details
                        html.Button(
                            id="login-submit-button", n_clicks=0, children="Login"
                        ),
                    ]
                )
            ],
        )
    # If button not clicked, do not unhide login container
    else:
        login_card = html.Div(id="login-container")

    return [login_card]


@callback(
    [Output("create-posts-container", "children")],
    [Input("login-submit-button", "n_clicks")],
    [State("input", "value"), State("password", "value")],
    # Prevent error from missing id since the login div is hidden
    suppress_callback_exceptions=True,
)
def update_output(n_clicks_login_submit, username, password):
    """
    Callback to unhide the fields for user to create post after user clicks "login-submit-button'.

    :param n_clicks_login_submit: Number of clicks of the login submit button
    :param username: Value from login username input field
    :param password: Value from login password input field
    :return: dbc card with login input components displayed in empty div in main layout
    """

    # Define dictionary 3 example login username and password combinations
    login_details = {
        "user": "password",
        "user1": "password1",
        "user2": "password2",
    }

    # If username and password combination match dictionary, unhide a post creation section
    if username in login_details and login_details[username] == password:
        # Create a dbc card for the user
        unhide_post_section = dbc.Container(
            fluid=True,
            children=[
                # Create green text to alert user if successful login
                html.Label(
                    ["Successful login! Scroll down to post."],
                    className="fw-bold text-success d-flex justify-content-center",
                ),
                html.Br(),
                # Title for post creation card section
                html.H4(
                    ["Post your hotel location"],
                    id="card-name",
                    className="card-title fw-bolder text-dark d-flex justify-content-center",
                ),
                # Add posts creation section card with input fields to fill
                dbc.Card(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            [
                                                dbc.CardHeader(
                                                    ["Hotel Information"],
                                                    class_name="d-flex justify-content-center",
                                                ),
                                                dbc.CardBody(
                                                    [
                                                        # Add input field and heading for hotel name
                                                        dbc.Label("Hotel Name"),
                                                        dbc.CardGroup(
                                                            [
                                                                dcc.Input(
                                                                    id="hotel-name",
                                                                    type="text",
                                                                    placeholder="Enter hotel name",
                                                                    style={
                                                                        "width": "400px"
                                                                    },
                                                                ),
                                                            ]
                                                        ),
                                                        html.Br(),
                                                        # Add input field and heading for hotel image
                                                        dbc.Label(
                                                            "Image of hotel or business"
                                                        ),
                                                        dbc.CardGroup(
                                                            [
                                                                dcc.Input(
                                                                    id="hotel-image-url",
                                                                    type="text",
                                                                    placeholder="Enter image url of your hotel or business",
                                                                    style={
                                                                        "width": "400px"
                                                                    },
                                                                ),
                                                            ]
                                                        ),
                                                        html.Br(),
                                                        # Add input field and heading for hotel location
                                                        dbc.Label(
                                                            "Country and Location"
                                                        ),
                                                        dbc.CardGroup(
                                                            [
                                                                dcc.Input(
                                                                    id="hotel-location",
                                                                    type="text",
                                                                    placeholder="Enter hotel country and location address",
                                                                    style={
                                                                        "width": "400px"
                                                                    },
                                                                ),
                                                            ]
                                                        ),
                                                        html.Br(),
                                                        # Add input field and heading for hotel description
                                                        dbc.Label("Description"),
                                                        dbc.CardGroup(
                                                            [
                                                                dcc.Input(
                                                                    id="hotel-description",
                                                                    type="text",
                                                                    placeholder="Enter hotel description",
                                                                    style={
                                                                        "width": "400px"
                                                                    },
                                                                ),
                                                            ],
                                                            style={"height": "100px"},
                                                        ),
                                                        html.Br(),
                                                        # Add input field and heading for hotel number of stars
                                                        dbc.Label("Number of stars"),
                                                        dbc.CardGroup(
                                                            [
                                                                dcc.Input(
                                                                    id="hotel-stars",
                                                                    type="number",
                                                                    placeholder="Enter number of stars",
                                                                    min=1,
                                                                    max=5,
                                                                    style={
                                                                        "width": "400px"
                                                                    },
                                                                ),
                                                            ]
                                                        ),
                                                        html.Br(),
                                                        # Add input field and heading for business email address
                                                        dbc.Label(
                                                            "Business Email Address"
                                                        ),
                                                        dbc.CardGroup(
                                                            [
                                                                dcc.Input(
                                                                    id="hotel-email",
                                                                    type="text",
                                                                    placeholder="Enter email address",
                                                                    min=1,
                                                                    style={
                                                                        "width": "400px"
                                                                    },
                                                                ),
                                                            ]
                                                        ),
                                                        html.Br(),
                                                        html.Label(
                                                            [
                                                                "Ensure all fields are complete"
                                                            ],
                                                            className="fw-bold text-danger d-flex justify-content-center",
                                                        ),
                                                        html.Br(),
                                                        # Add button to submit changes from all fields to callback
                                                        html.Button(
                                                            id="submit-location-button",
                                                            n_clicks=0,
                                                            children="Submit",
                                                            className="my-1 rounded border-secondary",
                                                            style={"width": "400px"},
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            ],
        )
    else:
        unhide_post_section = "Please input valid username and password"

    return [unhide_post_section]


@callback(
    [Output("added-posts-container", "children")],
    [Input("submit-location-button", "n_clicks")],
    [
        State("hotel-name", "value"),
        State("hotel-image-url", "value"),
        State("hotel-location", "value"),
        State("hotel-description", "value"),
        State("hotel-stars", "value"),
        State("hotel-email", "value"),
    ],
    suppress_callback_exceptions=True,
)
def add_post_hotel(
    n_clicks_add_post,
    hotel_name,
    hotel_image,
    hotel_location,
    hotel_description,
    hotel_stars,
    hotel_email,
):
    """
    Callback to update the empty div in layout with values entered and submitted in the posts form by user.

    :param hotel_name, hotel_name, hotel_location, hotel_description, hotel_stars, hotel_email:
        Values of each form field in the post creation entered by user
    :return: dbc card to replace empty div in layout with with submitted form values.
    """
    # If there is a value in every field, create a new post dbc card with entered details
    if all(
        value
        for value in [
            hotel_name,
            hotel_image,
            hotel_location,
            hotel_description,
            hotel_stars,
            hotel_email,
        ]
    ):
        # Create new dbc card updated with user-entered parameters
        added_post_card = dbc.Card(
            dbc.CardBody(
                [
                    html.H5(
                        f"{hotel_name}",
                        className="card-title d-flex justify-content-center",
                    ),
                    html.H6(f"{hotel_location}", className="card-subtitle"),
                    html.Img(src=hotel_image),
                    html.Br(),
                    html.Br(),
                    html.P(f"Description: {hotel_description}", className="card-text"),
                    html.P(f"{hotel_stars} Star Hotel", className="card-text"),
                    html.P(f"Contact Email: {hotel_email}", className="card-text"),
                ]
            ),
            # Increase bottom margin
            className="mb-3",
        )

    else:
        added_post_card = html.Div()

    return [added_post_card]
