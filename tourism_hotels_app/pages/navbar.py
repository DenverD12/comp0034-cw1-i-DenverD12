from dash import html, dcc, Dash, dash_table, Input, Output
import dash_bootstrap_components as dbc

CUSTOM_LOGO = "https://github.com/ucl-comp0035/comp0034-cw1-i-DenverD12/blob/main/tourism_hotels_app/images/custom_logo_tourism_hotels.png"


def Navbar():
    search_bar = dbc.Container([
                                dbc.Row(
                                    [
                                        dbc.Col(dbc.Input(type="search", placeholder="Search")),
                                        dbc.Col(
                                            dbc.Button(
                                                "Search", color="primary", className="ms-2", n_clicks=0
                                            ),
                                            width="auto",
                                        ),
                                    ],
                                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0"
                                )
                                ])

    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=CUSTOM_LOGO, height="30px")),
                            dbc.Col(dbc.NavbarBrand("TOURISM & HOSPITALITY", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.Row([
                    dbc.Col([
                        dbc.Nav([
                                dbc.NavItem(dbc.NavLink("Home", href="/")),
                                dbc.NavItem(dbc.NavLink("Trends Page", href="/pg2")),
                                dbc.NavItem(dbc.NavLink("Posts Page", href="/pg3")),
                                ])
                            ])
                        ]),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    search_bar,
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ],
            fluid=True,
        ),
        color="info",
        dark=True,
    )
    return navbar

