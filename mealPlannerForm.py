"""
This module defines the view for handling GET and POST requests for the 
meal planner feature of the Recipe and Meal Planner application.
"""
from flask import request, render_template, redirect, url_for
from flask.views import MethodView
from datetime import datetime, timedelta


class MealPlannerForm(MethodView):
    """
    Handles the meal planner form page.

    Methods:
    -------
    get(): Handles GET requests to the meal planner form page.
    post(): Handles POST requests to the meal planner form page.
    """


    def get(self):
        """
        Renders the meal planner form page.

        Returns:
        -------
        response : str
            The rendered HTML template for the meal planner form page.
        """
        title = request.args.get('title')  # Get title from query string
        image = request.args.get('image')  # Get image from query string
        return render_template("mealPlannerForm.html", recipe_title=title, recipe_image=image)
    
    
    def post(self):
        return redirect(url_for('search'))