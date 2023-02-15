"""Helper file with bootstrap navbar function."""
from dash import html
import dash_bootstrap_components as dbc

# Define logo with copyright-free example url
CUSTOM_LOGO = "https://cdn-icons-png.flaticon.com/512/293/293800.png?w=826&t \
    =st=1676386608~exp=1676387208~hmac=20c9a8d4eee9de4ed34a63a03b6c17a204d \
    bc89db4114323135959857c387789"


# Define navigation bar function
def Navbar():
    # Define search bar in a bootstrap container
    search_bar = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        # Add input field to type search queries
                        [dbc.Input(type="search", placeholder="Search")],
                        # Format spacing to neatly fit in the navbar band
                        className="ms-auto flex-nowrap mt-3 mt-md-0 gx-2",
                    ),
                    dbc.Col(
                        [  # Add button to submit the search
                            dbc.Button(
                                "Search", color="primary", className="ms-2", n_clicks=0
                            )
                        ],
                        width="auto",
                        className="ms-auto flex-nowrap mt-3 mt-md-0 border rounded px-2 ps-0 me-3 gx-4",
                    ),
                ],
                # Increase horizontal gutter spacing
                className="gx-1",
            ),
        ]
    )
    # Define dash bootstrap navbar
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and column to control vertical alignment of logo
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=CUSTOM_LOGO, height="30px")),
                            dbc.Col(
                                dbc.NavbarBrand(
                                    "TOURISM & HOSPITALITY", className="ms-2"
                                )
                            ),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    # Add a hyperlink to the first (home) page "pg1"
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Nav(
                                    [  # Add 3 navigation bar link objects with a link to each page
                                        dbc.NavItem([dbc.NavLink("Home", href="/")]),
                                        dbc.NavItem(dbc.NavLink("Trends", href="/pg2")),
                                        dbc.NavItem(dbc.NavLink("Posts", href="/pg3")),
                                    ]
                                )
                            ],
                            className="px-4 fw-bold gx-4",
                        )
                    ]
                ),
                # Toggler for navbar to collapse on small screens
                # Connected to the callback in main file with id
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    search_bar,
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ],
            # Set fluid to fill width of screen on all screen size
            fluid=True,
        ),
        # Change color of navbar to blue
        color="primary",
        # Make navbar text white for better visual
        dark=True,
    )
    return navbar
