"""Helper functions for creating the charts."""
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Global prepared dataset path for tourist arrivals
TOURISM_DATA_FILEPATH = Path(__file__).parent.parent.joinpath(
    'data', 'Tourism_arrivals_prepared.csv')
# Import global prepared dataframe from above dataset
df_arrivals_prepared = pd.read_csv(TOURISM_DATA_FILEPATH)


def bar_chart_top_x_tourism_countries(top_x_countries):
    """
    Create a bar chart showing the top 1 to 15 countries for highest average
    international tourist arrivals over the last 10 recorded years.

    Args:
        top_x_countries: Callback output for a number from 1 to 15
    Returns:
        fig_bar_chart_10_yr_average_topx: Plotly Express bar chart figure
    """
    # Specify the desired columns
    cols = [
            "Country Name", "Indicator Name",
            "10-year Average in tourist arrivals",
            ]

    # Define global dataframe of the prepared tourism dataset
    df_arrivals_10year_average = pd.read_csv(
                                             TOURISM_DATA_FILEPATH,
                                             usecols=cols
                                             )

    # Sort the values by "Average tourist arrivals in last 10 years" column descending order
    df_arrivals_ascending_10yr_average = df_arrivals_10year_average.sort_values(['10-year Average in tourist arrivals'], ascending=(False))

    df_arrivals_10yr_topx = df_arrivals_ascending_10yr_average.head(top_x_countries)

    # Create some title text for the bar chart in a variable
    title_text = f"Top {top_x_countries} countries for international tourist arrivals"
    # Create the plotly bar chart figure
    fig_bar_chart_10_yr_average_topx = px.bar(
                                               df_arrivals_10yr_topx,
                                               # Display corresponding country names in x axis
                                               x="Country Name",
                                               y="10-year Average in tourist arrivals",
                                               labels={"Country Name": "", "variable": "Indicator Name"},
                                               hover_name="Country Name",
                                               hover_data={
                                               # remove unwanted "Country Name" column from hover data
                                                           'Country Name': False,
                                                           },
                                               template="simple_white",
                                               )
    return fig_bar_chart_10_yr_average_topx


def create_choropleth_map(year_selected):
    """
    Create a choropleth map showing in terms of level on a color gradient
    what the different countries are in terms of tourist arrivals.

    Args:
        year_selected: Callback output of a number between 1995 to 2020
    Returns:
        fig_choropleth: Plotly Express choropleth map figure
    """
    # Create choropleth figure, note title not added
    ## Title added in main page layout to look better with responsive devices
    fig_choropleth = px.choropleth(df_arrivals_prepared, locations="Country Code",
                            color=str(year_selected),
                            hover_name="Country Name",
                            hover_data={
                                        # remove unwanted "Country Code" column from hover data
                                        'Country Code': False,
                                        },
                            projection='natural earth',
                            color_continuous_scale=px.colors.sequential.Plasma)
                            
                            
    # Center the choropleth figure title text
    fig_choropleth.update_layout(title=dict(font=dict(size=20), x=0.5, xanchor='center'),
    # Resize the choropleth figure to a larger size to view easier
                                 margin={"r": 10, "t": 10, "l": 0, "b": 0},
                                 )
    return fig_choropleth

def create_scatter_per_country():
    """
    
    """
    # Drop all columns without numeric data, other than Country Name
    # Also drop the 10-year Average in tourist arrivals column
    df_arrivals_prepared = \
        df_arrivals_prepared.drop([
                                   'Region', 'IncomeGroup',
                                   'Country Code',
                                   'Indicator Name',
                                   '10-year Average in tourist arrivals'
                                   ],
                                  axis=1)

    # Transpose dataframe, reset index to retrieve the column with years
    df_arrivals_transposed = df_arrivals_prepared.set_index('Country Name').T.reset_index()

    # Create line chart with markers
    fig_scatter_per_country = px.line(df_arrivals_transposed, x="index", y="Aruba", markers=True)

    return fig_scatter_per_country