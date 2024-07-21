"""
This module defines the view for handling GET requests for the 
search feature of the Recipe and Meal Planner application.
"""
import requests
from flask import request, render_template
from flask.views import MethodView

class Search(MethodView):
    """
    Handles the search for recipes via a web form.

    Methods:
    -------
    get(): Handles GET requests to the search page.
    """

    
    def __init__(self, app_id, app_key):
        """
        Initializes the Search class with the app id and app key for Edamam.
        
        Parameters:
        ----------
        app_id : str
            The app id for accessing the Edamam API
        app_key : str
            The API key for accessing the Edamam API.
        """
        self.app_id = app_id
        self.app_key = app_key
    

    def get(self):
        """
        Renders the search page.

        Returns:
        -------
        response : str
            The rendered HTML template for the search page.
        """
        print("Getting Recipes from the server")
        query = request.args.get('query')
        meal_type = request.args.get('meal-type')
        cuisine_type = request.args.get('cuisine-type')
        health = request.args.get('health')
        dish_type = request.args.get('dish-type')

        if query is None and (meal_type is None or cuisine_type is None or health is None or dish_type is None):
            query = "recipes"
        if meal_type is None:
            meal_type = ""
        if cuisine_type is None:
            cuisine_type = ""
        if health is None:
            health = ""
        if dish_type is None:
            dish_type = ""

        base_url="https://api.edamam.com/api/recipes/v2"
        params = {
            'type': "public",
            'q': query,
            'mealType': meal_type,
            'cuisineType': cuisine_type,
            'health': health,
            'dishType': dish_type,
            'app_id': self.app_id,
            'app_key': self.app_key,
            'random': True,
        }

        # filter out the None value parameters
        filtered_params = {param_key: param_value for param_key, param_value in params.items() if param_value != ""}
        query_string = '&'.join([f"{param_key}={param_value}" for param_key, param_value in filtered_params.items()])
        full_url = f"{base_url}?{query_string}"
        response = requests.get(full_url, params=filtered_params)
        search_results = response.json()
        if search_results:
            recipes = search_results.get('hits', [])
            return render_template('search.html', recipes=recipes)
        else:
            return 'Failed to fetch search results', 500
