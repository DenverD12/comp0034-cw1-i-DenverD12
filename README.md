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
## **Instructions for posts page in multi-page app**
### Login details for login:
- username is `user` and password is `password` for now. 
- there are 2 other combinations in the code for pg3.
- Since i did not have the time and ability to use learn external modules during the timeframe given to create databases to store the accounts, I could only store 3 example combinations. 
- Although this does not use the dataset as a visualisation, this page fulfills one of the requirements in the app and one of the goals of the app itself, which is for collaboration of hospitality businesses.
<br/>

The post page was added so users, hotel and hospitality business owners after viewing the dashboard and selecting a country to open their hotel, can post their location and country with contact details on this page.  
- It can be for an existing or upcoming planned location.
- This allows collaboration with other hospitality business owners for example for a posted hotel, a restaurant owner can see the post and contact the hotel owner to collaborate and simultaneously increase revenue and profits.
- In order to post, the user must login. 
- I added a working login section, that can be unhidden when the "login to post" button is clicked. The user then enters login details  
- The user can post their details by filling the form, and, when submit button is clicked, the post will update in the layout of the app itself.
- The other tiles are examples, and images were not used due to copyright. Also, I made it so the posts, resize and reorder to fit screen for smaller screens, which is something the target user wanted.
- In future, I would, with more time and ability to store items in a database, be able to have more actual posts stored and added to the layout.
## **Used in final app but functionality not fully complete**   
**A search bar and search button added to the navigation bar for multi-page searching**
<br/>
The search bar functionality does not currently search.   
It was supposed to be a final functionality to be added, but, due to the short timeframe given, I did not manage to make it search for items and return results for any page.  
However, the search bar ability to collapse callback on smaller screens such as phones works, and on smaller screens it will collapse to a button with 3 lines symbol which can be clicked to open the searchbar. 


<br/>

## **Bugs with plotly itself I could not fix**  
**Responsive ability of the choropleth figure itself**  
The choropleth map figure would not resize in width to fit small screen sizes such as mobile phones, despite the correct neccessary bootstrap responsive container settings. I also ensured the best settings in the plotly graph itself, however, I could not fix this.  
I checked online on forums and it seemed to be a problem/bug with plotly choropleth itself, rather than bootstrap, as every other chart updates as it should with the column layout 
The positive side is that the user can still drag the map to see any parts off the screen, but it is still somewhat visually unappealing.


## **Not used in final**:  
### **1. Horizontal bar chart for a single region selected instead of the treemap was investigated**  
<br/>

In order to see how it works, you can simply copy and paste below following code into the function `def create_tree_map(year_selected, region_name):` in the `create_charts.py` file.  
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
I did not use this chart, as the smaller number of arrivals countries sections were much too small.   
 However, the tree map chart was more visually clear in presenting the regions as it is proportional rather than accounting for exact value like stacked bar. Therefore, the tree map had more regions visible near the top end of number of arrivals, which is what the target audience was looking for in most of the questions. It also had the ability to click and zoom in on the smallest squares unlike the bar chart
A normal bar chart of each country was also considered, but there was the same issue with the stacked bar, as well as the main issue of too many bars for each region on a page and especially too much when "All regions" was chosen, which would be around 195 bars.
<br/>

### **2. Pie chart**  
- Again this was used in the same way as the stacked bar chart above and not used in the final for the same reasoning. It can also be pasted in the same function and update the return variable to see.  
- I decided not to use it for the same reasons as to why i didn't use the stacked bars.
- Mainly, the treemap won in ability to click each square to zoom in, thereby allowing selection of smallest squares.

```
    # Create plotly pie chart
    fig_pie_chart_region = px.pie(
        data_frame=filtered_df_by_region_ascending,
        values=f"{year_selected}",
        names="Country Name",
        color="Country Name",
        labels={
            "Country Name": "No. of arrivals in",
            "labels=": "",
        },  # Improve repeated country name and replace with informative text
        template="presentation",
        # Set figure dimensions, add hole and change size
        width=580,
        height=361,
        hole=0.25,
    )

    # Remove unneccesary and crowded percentage proportion labels
    fig_pie_chart_region.update_traces(
        textposition="none",
        # Add faint black lines to distinguish similar colored slices
        marker=dict(line=dict(color="#000000", width=0.1)),
    )
    # Add legend, change font and color, and reduce size
    fig_pie_chart_region.update_layout(
        legend=dict(font=dict(size=10, color="black")),
        legend_title=dict(font=dict(family="Courier", size=10, color="blue")),
    )
```

