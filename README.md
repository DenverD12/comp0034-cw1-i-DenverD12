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

Add any notes here (optional).

# Testing

Add evidence here (groups).
