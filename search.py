"""
This module defines the view for handling GET and POST requests for the 
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

        search_results = self.search_recipes(query)

        if search_results:
            recipes = search_results.get('hits', [])
            return render_template('search.html', recipes=recipes, query=query)
        else:
            return 'Failed to fetch search results', 500
        
    # Function to interact with the Edamam API to search for recipes
    def search_recipes(self, query):
        url="https://api.edamam.com/api/recipes/v2"
        params = {
            'type': "public",
            'q': query,
            'app_id': self.app_id,
            'app_key': self.app_key,
            'random': True,
        } 
        url = url + '?' + '&'.join([f"{k}={v}" for k, v in params.items() if v is not None])
        print("Full URL:", url)
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

