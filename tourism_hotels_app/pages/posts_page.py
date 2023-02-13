"""Contain the contents for the third page in multi-page app"""
import dash
from dash import html, dcc, Dash, dash_table, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import uuid
import os
import plotly.graph_objs as go

dash.register_page(__name__)


example_image_url = "http://www.example.com"

card_1 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Example Hotel Name", className="card-title d-flex justify-content-center"),
            html.H6("Example Country and Location", className="card-subtitle"),
            html.Img(src=example_image_url),
            html.Br(),
            html.Br(),
            html.P("Example Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", className="card-text"),
            html.P("5 Star Hotel", className="card-text"),
            html.P("Contact Email: email@gmail.com", className="card-text"),
        ]
    ),
    className="mb-3",
)

card_2 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Example Hotel Name", className="card-title d-flex justify-content-center"),
            html.H6("Example Country and Location", className="card-subtitle"),
            html.Img(src=example_image_url),
            html.Br(),
            html.Br(),
            html.P("Example Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", className="card-text"),
            html.P("3 Star Hotel", className="card-text"),
            html.P("Contact Email: email@gmail.com", className="card-text"),
        ]
    ),
    className="mb-3",
)

card_3 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Example Hotel Name", className="card-title d-flex justify-content-center"),
            html.H6("Example Country and Location", className="card-subtitle"),
            html.Img(src=example_image_url),
            html.Br(),
            html.Br(),
            html.P("Example Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", className="card-text"),
            html.P("4 Star Hotel", className="card-text"),
            html.P("Contact Email: email@gmail.com", className="card-text"),
        ]
    ),
    className="mb-3",
)


layout = dbc.Container(
        fluid=True,
        children=[
            # First row here
            dbc.Row([
                html.H4(
                        ["Existing or Paanned Hospitality Location Posts"], id="card-name", 
                        className="card-title text-dark d-flex justify-content-center"
                            ),
                html.H5(["Post your location and details to collaborate with others in the hospitality sector!"],
                        className="d-flex justify-content-center lead"),
                html.Br(),
                html.Br(),

                # Example existing (already posted) locations
            
                    dbc.Col([card_1], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                    dbc.Col([card_2], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                    dbc.Col([card_3], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                    dbc.Col([card_1], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                    dbc.Col([card_2], width=4, xs=12, sm=12, md=6, lg=4, xl=4),
                    
                # Have empty div to hold any new locations posted by user
                    dbc.Col(html.Div(id="added-posts-container"), width=4, xs=12, sm=12, md=6, lg=4, xl=4),

                    ], justify="center"),

            html.H5(["Have your own location to add? Login to post your own!"],
                     className="text-primary fw-bold d-flex justify-content-center"),
            
            dbc.Row([
                dbc.Col([
                    html.Button(['Login to post'],
                                                    id="login-unhide-button", n_clicks=0,
                                                    className="bg-info p-2 border rounded border-secondary"),
                        ], 
                    width="auto")],
                    justify="center",
                    ),
            
            dbc.Row([
                dbc.Col([
                        html.Div(id="login-container"),
                        html.Div(id='output-container')
                        ], 
                    width="auto")],
                    justify="center",
                    ),
])

@callback(
    [Output("added-posts-container", "children")],
    [Input("submit-location-button", "n_clicks")],
    [State('hotel-name', 'value'),
     State('hotel-image-url', 'value'),
     State('hotel-location', 'value'),
     State('hotel-description', 'value'),
     State('hotel-stars', 'value'),
     State('hotel-email', 'value'),
     ],
    suppress_callback_exceptions=True
)
def add_post_hotel(n_clicks_add_post, hotel_name, hotel_image, hotel_location, hotel_description, hotel_stars, hotel_email):
    
    added_post_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5(f"{hotel_name}", className="card-title d-flex justify-content-center"),
            html.H6(f"{hotel_location}", className="card-subtitle"),
            html.Img(src=hotel_image),
            html.Br(),
            html.Br(),
            html.P(f"{hotel_description}", className="card-text"),
            html.P(f"{hotel_stars} Star Hotel", className="card-text"),
            html.P(f"{hotel_email}", className="card-text"),
        ]
    ),
    className="mb-3",
)

    return [added_post_card]
    



@callback(
    [Output("login-container", "children")],
    [Input("login-unhide-button", "n_clicks")],
    suppress_callback_exceptions=True
)
def unhide_login_fields(n_clicks_login_unhide):

    # If button clicked an odd number of times, unhide login container
    if n_clicks_login_unhide:
        login_card = dbc.Container(
        children=[
            dbc.CardBody(
                    [
                     dcc.Input(id='input', placeholder='Enter Username', type='text'),
                     dcc.Input(id='password', placeholder='Enter Password', type='password'),
                     html.Button(id='login-submit-button', n_clicks=0, children='Login')
                    ]
                )
            ],
        )
    else:
        login_card = html.Div(id='login-container')
                            
    return [login_card]

@callback(
    [Output('output-container', 'children')],
    [Input('login-submit-button', 'n_clicks')],
    [State('input', 'value'),
     State('password', 'value')],
    # Prevent error from missing id since the login div is hidden
    suppress_callback_exceptions=True
)
def update_output(n_clicks, username, password):
    
    login_details = {
                "user": "password",
                "user1": "password1",
                "user2": "password2",
            }
    
    if username in login_details and login_details[username] == password:
        # Create a dbc card for the user
        unhide_post_section = dbc.Container(
            fluid=True,
        children=[
            html.Label(["Successful login! Scroll down to post."], className="fw-bold text-success d-flex justify-content-center"),
            html.Br(),
            html.H4(
                    ["Post your hotel location"], id="card-name", 
                     className="card-title fw-bolder text-dark d-flex justify-content-center"
                    ),
            dbc.Card(
                    [
                    dbc.Row(
                            [
                             dbc.Col([
                                 dbc.Card(
                                     [
                                         dbc.CardHeader(["Hotel Information"],
                                         class_name="d-flex justify-content-center"),
                                         dbc.CardBody(
                                             [  
                                                dbc.Label("Hotel Name"),
                                                 dbc.CardGroup(
                                                        [
                                                         dcc.Input(id="hotel-name", 
                                                         type="text",
                                                         placeholder="Enter hotel name",
                                                         style={
                                                            "width": "400px"
                                                             }),
                                                        ]
                                                 ),
                                                 html.Br(),
                                                 dbc.Label("Image of hotel or business"),
                                                 dbc.CardGroup(
                                                        [
                                                         dcc.Input(id="hotel-image-url",
                                                         type="text",
                                                         placeholder="Enter image url of your hotel or business",
                                                         style={
                                                            "width": "400px"
                                                             }),
                                                        ]
                                                 ),
                                                 html.Br(),
                                                 dbc.Label("Country and Location"),
                                                 dbc.CardGroup(
                                                        [
                                                         dcc.Input(id="hotel-location",
                                                         type="text",
                                                         placeholder="Enter hotel country and location address",
                                                         style={
                                                            "width": "400px"
                                                             }),
                                                        ]
                                                 ),
                                                 html.Br(),
                                                 dbc.Label("Description"),
                                                 dbc.CardGroup(
                                                        [
                                                         dcc.Input(id="hotel-description",
                                                         type="text",
                                                         placeholder="Enter hotel description",
                                                         style={
                                                            "width": "400px"
                                                             }),
                                                        ],
                                                        style={
                                                            "height": "100px"
                                                             }
                                                 ),
                                                 html.Br(),
                                                 dbc.Label("Number of stars"),
                                                 dbc.CardGroup(
                                                        [
                                                         dcc.Input(id="hotel-stars",
                                                         type="number",
                                                         placeholder="Enter number of stars", 
                                                         min=1, max=5,
                                                         style={
                                                            "width": "400px"
                                                             }),
                                                        ]
                                                 ),
                                                 html.Br(),
                                                 dbc.Label("Business Email Address"),
                                                 dbc.CardGroup(
                                                        [
                                                         dcc.Input(id="hotel-email",
                                                         type="text",
                                                         placeholder="Enter email address",
                                                         min=1,
                                                         style={
                                                            "width": "400px"
                                                             }),
                                                        ]
                                                 ),
                                                 html.Br(),
                                                 html.Button(id='submit-location-button', 
                                                 n_clicks=0, children='Submit', 
                                                 className="my-1 rounded border-secondary",
                                                 style={"width": "400px"})
                                             ]
                                         ),
                                     ]
                                 ),
                                ]
                                )
                            ]
                        )

                    ]
                )
            ],
        )
    else:
        unhide_post_section = "Please input valid username and password"
         
    return [unhide_post_section]


