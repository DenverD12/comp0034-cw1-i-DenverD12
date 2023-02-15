[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9733923&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
2. Create and then activate a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [the pip documentation](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. 


# Set-up instructions

Add any instructions here for the markers on how to setup and run your Dash app.  

1. First setup and activate a virtual environment.
2. Secondly, in the terminal run code: `pip install -r requirements.txt` to install dependencies
3. Then, in the terminal run code: `pip install setup.py`
4. Next, run `tourism_hotels_dash_app.py` for the main multi-page dash app

- **Note: It will show callback ID errors raised. Ignore these, as they are due to an initially hidden container in the "Posts" page. I added a `suppress_callback_exceptions=True` argument to the callbacks but strangely, the error sometimes remains, but the app works as expected.**
- **Also, do not individually run the individual page files themselves (`pg1.py`, `pg2.py`, `pg3.py`) because importing the charts will show module not found error, instead only run the main app file `tourism_hotels_app.py`.**

<br/>

# **URL to my GitHub repo**
**https://github.com/ucl-comp0035/comp0034-cw1-i-DenverD12**

# Visualisation design
Evidence in `visualisation-design.pdf` file  

<br/>

# Dash app

## **Used in final app but functionality not fully complete**   
**A search bar and search button added to the navigation bar for multi-page searching**
<br/>
The search bar functionality does not currently search.   
It was supposed to be a final functionality to be added, but, due to the short timeframe given, I did not manage to make it search for items and return results for any page.  
However, the search bar ability to collapse callback on smaller screens such as phones works, and on smaller screens it will collapse to a button with 3 lines symbol which can be clicked to open the searchbar. 


<br/>

## **Not used in final**:  
**Horizontal bar chart for a single region selected instead of the pie chart was investigated**  
<br/>

In order to see how it works, you can simply copy and paste below following code into the function `def create_pie_chart(year_selected, region_name):` in the `create_charts.py` file.  
Note: also change the output from `fig_pie_chart_region` to `fig_horizontal_bar`. This will output the hoizontal bar instead of the pie chart.
**Here is the code to copy and paste**:
```
filtered_df_by_region_ascending = filtered_df_by_region.sort_values(
        [f"{year_selected}"], ascending=(True)
    )
    fig_horizontal_bar_region = px.bar(
        filtered_df_by_region_ascending,
        x=f"{year_selected}",
        y="Region",
        color="Country Name",
        # Make horizontal orientation
        orientation="h",
        # Remove axis title that says "Region"
        labels={
            "Region": "",
        },
    )
```
I did not use this chart, as the smaller number of arrivals countries sections were much too small, just like the pie chart. However, the pie chart was more visually clear in presenting the regions as it is proportional rather than accounting for exact value like stacked bar. Therefore, the pie chart had more regions visible near the top end of number of arrivals, which is what the target audience was looking for in most of the questions.  
A normal bar chart of each country was also considered, but there was the same issue with the stacked bar, as well as the main issue of too many bars for each region on a page and especially too much when "All regions" was chosen, which would be around 195 bars.
<br/>

## **Bugs with plotly itself I could not fix**  
**Responsive ability of the choropleth figure itself**  
The choropleth map figure would not resize in width to fit small screen sizes such as mobile phones, despite the correct neccessary bootstrap responsive container settings. I also ensured the best settings in the plotly graph itself, however, I could not fix this.  
I checked online on forums and it seemed to be a problem/bug with plotly choropleth itself, rather than bootstrap, as every other chart updates as it should with the column layout 
The positive side is that the user can still drag the map to see any parts off the screen, but it is still somewhat visually unappealing.