"""
This module defines the view for handling GET requests for 
displaying all the meals for a weekly meal planner of the Recipe and Meal Planner application.
"""
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


    def get(self):
        """
        Renders the meal planner page.

        Retrieves the recipes from the model, and renders the meal planner page with the recipe data.
        
        Returns:
        -------
        response : str
            The rendered HTML template for the meal planner page with all the recipes.
        """
        model=mpmodel.get_model()
        recipes = [dict(id=row[0], recipe_id=row[1], recipe_title=row[2], recipe_url=row[3], recipe_day=row[4], recipe_meal=row[5]) for row in model.select()]
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
        
        recipe = json.loads(request.data)
        id = recipe['id']
        if id:
            model = mpmodel.get_model()
            model.delete(id)
            return jsonify({})