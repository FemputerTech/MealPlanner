"""
This module defines the view for handling GET requests for 
displaying all the meals for a weekly meal planner of the Recipe and Meal Planner application.
"""
import requests
from flask import request, render_template, jsonify
from flask.views import MethodView
import mpmodel
import json


class MealPlanner(MethodView):
    """
    Handles the display of weekly meals.

    Methods:
    -------
    get(): Handles GET requests to the meal planner page.
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
        Renders the meal planner page.

        Retrieves the recipes from the model, and renders the meal planner page with the recipe data.
        
        Returns:
        -------
        response : str
            The rendered HTML template for the meal planner page with all the recipes.
        """
        day = request.args.get('day')
        model=mpmodel.get_model()
        recipes = [dict(id=row[0], recipe_id=row[1], recipe_title=row[2], recipe_url=row[3], recipe_day=row[4], recipe_meal=row[5]) for row in model.select(day)]
        
        for recipe in recipes:
            recipe['recipe_image'] = self.getImageUrl(recipe['recipe_id'])  
        
        return render_template("mealPlanner.html", recipes=recipes)
    

    def delete(self):
        """
        Parses the request data to retrieve the recipe ID, deletes the corresponding recipe
        from the model, and returns an empty JSON response.

        Returns:
        -------
        response : flask.Response
            An empty JSON response indicating the deletion was successful.
        """
        print("deleting....")
        recipe = json.loads(request.data)
        id = recipe['id']
        if id:
            model = mpmodel.get_model()
            model.delete(id)
            return jsonify({})
        
    
    def getImageUrl(self, id):
        full_url = f"https://api.edamam.com/api/recipes/v2/{id}"
        params = {
            'type': "public",
            'app_id': self.app_id,
            'app_key': self.app_key,
        }
        response = requests.get(full_url, params=params)
        results = response.json()
        if results:
            recipe_image = results['recipe']['image']
            return recipe_image
        else:
            return 'Failed to fetch recipe results', 500

