"""
This module defines the view for handling DELETE requests for the 
weekly meals feature of the Recipe and Meal Planner application.
"""
from flask import request, jsonify
from flask.views import MethodView
import mpmodel
import json


class Delete(MethodView):
    """
    Handles the removal of recipes in the weekly meals view.

    Methods:
    -------
    delete(): Handles DELETE requests in the weekly meals page.
    """


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
        print("recipe:", recipe)
        id = recipe['id']
        if id:
            model = mpmodel.get_model()
            model.delete(id)
            return jsonify({})
