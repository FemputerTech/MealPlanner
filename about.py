"""
This module defines the view for handling GET requests to the about page
of the Recipe and Meal Planner application.
"""
from flask import render_template
from flask.views import MethodView


class About(MethodView):
    """
    Handles the about page.

    Methods:
    -------
    get(): Handles GET requests to the about page.
    """
    
    
    def get(self):
        """
        Renders the about page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the about page.
        """
        return render_template("about.html")