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

        Retrieves the selected week from the request arguments, fetches the corresponding
        recipes from the model, and renders the meal planner page with the recipe data.
        
        Returns:
        -------
        response : str
            The rendered HTML template for the meal planner page with the selected week's recipes.
        """
        selected_week = request.args.get('week_start')
        model=mpmodel.get_model()
        recipes = [dict(id=row[0], recipe_id=row[1], recipe_title=row[2], recipe_url=row[3], recipe_week_start=row[4], recipe_week_end=row[5], recipe_day=row[6], recipe_meal=row[7]) for row in model.select_recipe(selected_week)]
        return render_template("mealPlanner.html", week_start=selected_week, recipes=recipes)
    

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