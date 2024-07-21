"""
This module defines the view for handling GET and POST requests for the 
meal planner feature of the Recipe and Meal Planner application.
"""
from flask import request, render_template, redirect, url_for
from flask.views import MethodView
from datetime import datetime, timedelta
from urllib.parse import urlparse
import mpmodel


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
        url = request.args.get('url')  # Get url from query string
        ref = request.args.get('ref')
        
        parsed_ref = urlparse(ref)
        recipe_id = parsed_ref.path.split('/')[-1]

        return render_template("mealPlannerForm.html", recipe_title=title, recipe_image=image, recipe_url=url, recipe_id = recipe_id)
    
    
    def post(self):
        """
        Handles form submissions to add a recipe to the meal planner.
        
        Retrieves the recipe details and meal plan information from the form,
        then inserts the data into the model and redirects to the search page.

        Returns:
        -------
        A redirect response to the search page.
        """
        recipe_id = request.form.get('recipe_id')
        recipe_title = request.form.get('recipe_title')
        recipe_url = request.form.get('recipe_url')
        recipe_week_start = request.form.get('week_start')
        recipe_day = request.form.get('day')
        recipe_meal = request.form.get('meal')

        recipe_week_start = datetime.strptime(recipe_week_start, '%a %b %d %Y')
        recipe_week_end = recipe_week_start + timedelta(days=6)

        # formmatting to strings
        recipe_week_start = recipe_week_start.strftime('%a %b %d %Y')
        recipe_week_end = recipe_week_end.strftime('%a %b %d %Y')

        model = mpmodel.get_model()
        model.insert_recipe(recipe_id, recipe_title, recipe_url, recipe_week_start, recipe_week_end, recipe_day, recipe_meal)
        return redirect(url_for('search'))