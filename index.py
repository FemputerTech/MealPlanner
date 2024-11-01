"""
This module defines the view for handling GET requests to the home page
of the Recipe and Meal Planner application.
"""
from flask import render_template
from flask.views import MethodView
from data import popular_top, popular_bottom


class Index(MethodView):
    """
    Handles the index (home) page.

    Methods:
    -------
    get(): Handles GET requests to the index (home) page.
    """
    
    
    def get(self):
        """
        Renders the index (home) page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the index page.
        """
        return render_template("index.html", popularTop=popular_top, popularBottom=popular_bottom)