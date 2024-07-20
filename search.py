"""
This module defines the view for handling GET and POST requests for the 
search feature of the Recipe and Meal Planner application.
"""
import requests
from flask import request, render_template
from flask.views import MethodView
import json

class Search(MethodView):
    """
    Handles the search for recipes via a web form.

    Methods:
    -------
    get(): Handles GET requests to the search page.
    post(): Handles POST requests to the search page.
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
        search_results = self.search_recipes("recipes")
        if search_results:
            recipes = search_results.get('hits', [])
            return render_template('search.html', recipes=recipes)
        else:
            return 'Failed to fetch search results', 500


    def post(self):
        query = request.form.get('query')
        meal_type = request.form.get('meal-type')
        cuisine_type = request.form.get('cuisine-type')
        health = request.form.get('health')
        dish_type = request.form.get('dish-type')

        print("query:", query)
        print("meal type:", meal_type)
        print("cuisine type:", cuisine_type)
        print("health:", health)
        print("dish type:", dish_type)

        search_results = self.search_recipes(query, meal_type, cuisine_type, health, dish_type)

        if search_results:
            recipes = search_results.get('hits', [])
            if query == None:
                query = ""
            return render_template('search.html', recipes=recipes, query=query)
        else:
            return 'Failed to fetch search results', 500
        
        
    # Function to interact with the Edamam API to search for recipes
    def search_recipes(self, query, meal_type, cuisine_type, health, dish_type):
        print("searching for recipes...")
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
        print("Full URL:", full_url)
        response = requests.get(full_url, params=filtered_params)

        if response.status_code == 200:
            return response.json()
        else:
            return None

