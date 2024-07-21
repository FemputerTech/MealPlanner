"""
This application is a recipe and meal planning application that helps users
find recipes, plan meals for the week, and manage their meal plans.

The application uses Flask to create a web interface and includes several modules:
- Index: Handles the main landing page
- Search: Manages recipe searches
- Recipe: Displays individual recipes
- MealPlanner: Facilitates meal planning
- WeeklyMeals: Displays weekly meal plans
- Delete: Handles the deletion of recipes in weekly meals

Environment Variables:
- APP_ID: Required for accessing external recipe APIs.
- APP_KEY: Required for accessing external recipe APIs

To run the application, execute this script.
"""
import os
import flask
from index import Index
from about import About
from search import Search
from mealPlannerForm import MealPlannerForm
from mealPlanner import MealPlanner


# Initializes the Flask application
app = flask.Flask(__name__)


# Retrieve API key from environment variables
APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')


# URL routing for the main landing page
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET']
                 )


# URL routing for the about page
app.add_url_rule('/about',
                 view_func=About.as_view('about'),
                 methods=['GET']
                 )


# URL routing for the search functionality 
app.add_url_rule('/search',
                 view_func=Search.as_view('search', app_id=APP_ID, app_key=APP_KEY),
                 methods=['GET'])


# URL routing for the meal planner form
app.add_url_rule('/meal-planner-form',
                 view_func=MealPlannerForm.as_view('meal-planner-form'),
                 methods=['GET', 'POST'])


# URL routing for the meal planner
app.add_url_rule('/meal-planner',
                 view_func=MealPlanner.as_view('meal-planner', app_id=APP_ID, app_key=APP_KEY),
                 methods=['GET', 'DELETE'])


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)