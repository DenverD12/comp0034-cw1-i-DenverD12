"""Helper functions for creating the charts."""
from pathlib import Path
import pandas as pd
import math
import plotly.express as px
import plotly.graph_objs as go
import helper_functions as helper


# Create custom colorscale for choropleth map to match overall blue theme
custom_colorscale = [[0.0, "#003366"], [0.5, "#007bff"], [1.0, "#87ceeb"]]

# Global prepared dataset path for tourist arrivals
TOURISM_DATA_FILEPATH = Path(__file__).parent.parent.joinpath(
    "tourism_hotels_app", "data", "Tourism_arrivals_prepared.csv"
)
# Import global prepared dataframe from above dataset
df_arrivals_prepared = pd.read_csv(TOURISM_DATA_FILEPATH)


def create_choropleth_map(year_selected, selected_region):
    """
    Create a choropleth map showing in terms of level on a color gradient
    what the different countries are in terms of tourist arrivals.

    Args:
        year_selected: Callback output of a number between 1995 to 2020
        selected_region: Callback output of a region name as a string
    Returns:
        fig_choropleth: Plotly Express choropleth map figure for selected year and region
    """
    if selected_region == "All regions":
        filtered_df_by_region = df_arrivals_prepared
    else:
        # Filter by region if a region selected
        filtered_df_by_region = df_arrivals_prepared[
            df_arrivals_prepared["Region"] == selected_region
        ]

    # Create choropleth figure, note title not added
    ## Title added in main page layout to look better with responsive devices
    fig_choropleth = px.choropleth(
        filtered_df_by_region,
        locations="Country Code",
        color=str(year_selected),
        hover_name="Country Name",
        hover_data={
            # remove unwanted "Country Code" column from hover data
            "Country Code": False,
        },
        projection="natural earth",
        color_continuous_scale=custom_colorscale,
        labels={f"{str(year_selected)}": "No. of arrivals in <br>Millions"},
    )

    fig_choropleth.update_layout(
        # Resize choropleth figure to a larger size to view easier
        margin={"r": 10, "t": 10, "l": 0, "b": 0},
    )

    # Add shape and annotation to show missing data color for clarity
    fig_choropleth.add_shape(
        type="rect",
        x0=1.157,
        y0=0.02,
        x1=1.208,
        y1=0.092,
        xref="paper",
        yref="paper",
        fillcolor="#E5ECF6",
        line_width=0.1,
    )
    fig_choropleth.add_annotation(
        text="Unavailable<br>Data",
        x=1.180,
        y=0.145,
        xref="paper",
        yref="paper",
        yanchor="middle",
        xanchor="center",
        showarrow=False,
    )

    # Add text to instruct user how to use
    fig_choropleth.add_annotation(
        text="(Tip: Zoom in, drag and hover to see country names)",
        x=0.5,
        y=0.05,
        xref="paper",
        yref="paper",
        yanchor="middle",
        xanchor="center",
        showarrow=False,
        font=dict(size=18, color="blue"),
    )

    # Increase size of map and colourbar
    fig_choropleth.update_layout(
        autosize=False,
        margin=dict(l=0, r=0, b=0, t=0, pad=4, autoexpand=True),
        width=800,
        height=474,
    )

    return fig_choropleth


def create_tree_map(year_selected, region_name):
    """
    Create a tree map showing each country as a proportion for a specific
    year and region selected.

    Args:
        year_selected: Callback output of a number between 1995 to 2020
        selected_region: Callback output of a region name as a string
    Returns:
        fig_tree_map_regional: Plotly Express tree map figure for selected year and region
    """
    df_arrivals = df_arrivals_prepared

    # Filter dataset by region only if a region selected
    if region_name == "All regions":
        filtered_df_by_region = df_arrivals
    else:
        filtered_df_by_region = df_arrivals_prepared[
            df_arrivals_prepared["Region"] == region_name
        ]
        title_text = f"Distribution in arrivals in {region_name}"

    filtered_df_by_region_ascending = filtered_df_by_region.sort_values(
        [f"{year_selected}"], ascending=(True)
    )

    # Create tree map plotly figure
    fig_tree_map_regional = px.treemap(
        filtered_df_by_region_ascending,
        path=["Country Name"],
        values=f"{year_selected}",
        width=650,
        height=370,
        color=f"{year_selected}",
        template="simple_white",
        color_continuous_scale=custom_colorscale,
    )

    # Define custom hover template for clarity on country and data type
    hovertemplate = "<b>%{label} </b><br> Total arrivals: %{value:.2f}"

    # update trace with custom hover template
    fig_tree_map_regional.update_traces(
        hovertemplate=hovertemplate, textinfo="label+value"
    )

    # Add text to instruct user how to use
    fig_tree_map_regional.add_annotation(
        text="Hover over a square to see more details<br>Click any rectangle to zoom and focus",
        x=0.5,
        y=-0.15,
        xref="paper",
        yref="paper",
        yanchor="middle",
        xanchor="center",
        showarrow=False,
        font=dict(size=16, color="blue"),
    )

    # Update legend of colorscale to informative text
    fig_tree_map_regional.update_layout(
        coloraxis_colorbar=dict(title="No. of<br>arrivals<br>in Millions")
    )

    return fig_tree_map_regional


def bar_chart_top_x_tourism_countries(top_x_countries):
    """
    Create a bar chart showing the top 1 to 15 countries for highest average
    international tourist arrivals over the last 10 recorded years.

    Args:
        top_x_countries: Callback output of a number from 1 to 15
    Returns:
        fig_bar_chart_10_yr_average_topx: Plotly Express bar chart figure
    """
    # Specify desired columns
    cols = [
        "Country Name",
        "Indicator Name",
        "10-year Average in tourist arrivals",
    ]

    # Define global dataframe of the prepared tourism dataset
    df_arrivals_10year_average = pd.read_csv(TOURISM_DATA_FILEPATH, usecols=cols)

    # Sort the values by "Average tourist arrivals in last 10 years" column descending order
    df_arrivals_ascending_10yr_average = df_arrivals_10year_average.sort_values(
        ["10-year Average in tourist arrivals"], ascending=(False)
    )

    df_arrivals_10yr_topx = df_arrivals_ascending_10yr_average.head(top_x_countries)

    # Create the plotly bar chart figure
    fig_bar_chart_10_yr_average_topx = px.bar(
        df_arrivals_10yr_topx,
        # Display corresponding country names in x axis
        x="Country Name",
        y="10-year Average in tourist arrivals",
        labels={
            "Country Name": "",
            "10-year Average in tourist arrivals": "10-year Average in arrivals",
        },
        hover_name="Country Name",
        hover_data={
            # Remove unwanted "Country Name" label from hover data
            "Country Name": False,
        },
        template="simple_white",
        # Set bars to exact colour of Bootstrap 'primary' blue
        color_discrete_sequence=["#007bfa"],
    )

    # Remove the x-axis labels and tick lines
    fig_bar_chart_10_yr_average_topx.update_xaxes(ticklen=0)

    return fig_bar_chart_10_yr_average_topx


def create_line_per_country(country_name):
    """
    Create a line plot with markers for given country name.

    Args:
        country_name: Callback output of a selected country name as a string
    Returns:
        fig_line_per_country: Plotly line chart with markers figure for selected country

    """
    # Drop unwanted columns, transpose dataframe using helper function
    df_arrivals_transposed = helper.transpose_df_arrivals_prepared()

    # Create line chart with markers
    fig_line_per_country = px.line(
        df_arrivals_transposed,
        x="index",
        y=country_name,
        # Update labels for clarity, replace repeated country name
        labels={"index": "Year", f"{country_name}": "Number of Arrivals"},
        # Enable markers on line
        markers=True,
        template="simple_white",
        # Decrease height of chart to align with the stats card column
        height=405,
    )
    # Make line color 'primary' blue consistent with navbar
    fig_line_per_country.update_traces(line_color="#007bff")

    # Get y value for covid-19 year 2020
    value_2020_covid = df_arrivals_transposed.loc[25, f"{country_name}"]

    # If there is 2020 data, add annotation to inform user
    if not math.isnan(value_2020_covid):
        fig_line_per_country.add_annotation(
            text="<b>Covid-19 Year</b>",
            # Set x to row index number
            x=25,
            y=value_2020_covid,
            yanchor="bottom",
            xanchor="right",
            arrowhead=1,
            showarrow=True,
        )
    else:
        fig_line_per_country

    return fig_line_per_country


def create_line_chart_compare_countries(country_name_1, country_name_2):
    """
    Create 2 line plots on same chart for 2 given country names.

    Args:
        country_name_1: Callback output of first selected country name as a string
        country_name_2: Callback output of second selected country name as a string
    Returns:
        fig_line_chart_compare_countries: Plotly go line chart figure with 2 lines for each selected country
    """
    # Drop unwanted columns, transpose dataframe using helper function
    df_arrivals_transposed = helper.transpose_df_arrivals_prepared()

    # Define two countries to plot given as parameters
    countries = [f"{country_name_1}", f"{country_name_2}"]

    # Create a trace for each country
    traces = [
        go.Scatter(
            x=df_arrivals_transposed["index"],
            y=df_arrivals_transposed[country],
            mode="lines",
            name=country,
        )
        for country in countries
    ]
    # Assign blue color to the first trace and green to the second
    traces[0]["line"]["color"] = "blue"
    traces[1]["line"]["color"] = "green"

    # Create the combined line chart figure
    layout = go.Layout(
        xaxis_title="Year",
        yaxis_title="Number of Arrivals",
        template="simple_white",
    )

    # Plot the line chart figure
    fig_line_chart_compare_countries = go.Figure(data=traces, layout=layout)

    return fig_line_chart_compare_countries
