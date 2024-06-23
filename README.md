# Welcome to my Recipe and Meal Planner App!

## About

API: [Spoonacular API](https://spoonacular.com/food-api/docs)

Description: Develop a recipe and meal planning application that helps users find recipes and plan meals.

# Search for a recipe

You can search by food, cuisine, diet, intolerances, and type.

## Developement Setup

### Set up virtual environment

1. Install the virtual environment `virtualenv -p python3 env`
2. Activate the environment in your shell `source env/bin/activate`
3. Install dependencies `pip3 install -Ur requirements.txt`
4. Select the python interpreter for the virtual environment

### Running the application locally

1. create a local environment variable for API_KEY
   `export API_KEY=<the api key>`
2. create a local environment variable for GOOGLE_APPLICATION_CREDENTIALS
   `export GOOGLE_APPLICATION_CREDENTIALS="cloud-leicht-mleicht-key.json"`
3. run the with python `python3 app.py`
