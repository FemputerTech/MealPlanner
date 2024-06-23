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
    def get(self):
        """
        Renders the search page.

        Returns:
        -------
        response : str
            The rendered HTML template for the search page.
        """
        return render_template('search.html')
    
    def post(self):
        query = request.form.get('query')
        return render_template('search.html', query=query)

