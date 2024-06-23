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
- API_KEY: Required for accessing external recipe APIs

To run the application, execute this script.
"""
import os
import flask
from index import Index
from search import Search


# Initializes the Flask application
app = flask.Flask(__name__)


# Retrieve API key from environment variables
API_KEY = os.getenv('API_KEY')


# URL routing for the main landing page
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET']
                 )


# URL routing for the search functionality 
app.add_url_rule('/search',
                 view_func=Search.as_view('search'),
                 methods=['GET', 'POST'])


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)