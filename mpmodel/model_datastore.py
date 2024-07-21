"""
This module defines the model class for interacting with GCP Datastore.
"""
from .Model import Model
from google.cloud import datastore


def from_datastore(entity):
    """
    Convert a Datastore entity to a Python dictionary.

    Parameters:
    ----------
    entity : google.cloud.datastore.Entity
        The Datastore entity to convert.

    Returns:
    -------
    list or None
        A list containing the properties of the Datastore entity.
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity.key.id, entity['recipe_id'], entity['recipe_title'], entity['recipe_url'], entity['recipe_day'], entity['recipe_meal']]


class model(Model):
    """
    The model class for interacting with GCP Datastore.

    Methods:
    -------
    __init__():
        Initialize the model with a GCP Datastore client.

    select_recipe(selected_week):
        Retrieves all recipes from the datastore for a selected week.

    insert_recipe(recipe_id, recipe_title, recipe_url, recipe_day, recipe_meal):
        Inserts a recipe into the datastore.

    delete(entity_key):
        Deletes a recipe from the datastore.
    """


    def __init__(self):
        """
        Initialize the model with a GCP Datastore client.
        """
        self.client = datastore.Client('cloud-mealplanner-leicht')


    def select(self):
        """
        Retrieves all recipes from the datastore.

        Returns:
        -------
        list of lists
            A list containing all rows of recipes from the datastore.
        """
        query = self.client.query(kind = 'Recipes')
        entities = query.fetch()
        return [from_datastore(entity) for entity in entities]


    def insert_recipe(self, recipe_id, recipe_title, recipe_url, recipe_day, recipe_meal):
        """
        Insert a recipe into datastore.

        Parameters:
        ----------
        recipe_id : string
            the id of the recipe.
        recipe_title : str
            The title of the recipe.
        recipe_url: str
            The URL of the recipe.
        recipe_day: str
            The day of the week the recipe is planned for.
        recipe_meal: str
            The type of meal the recipe is planned for.
        
        Returns:
        -------
        bool
            True if the insertion is successful.
        """
        key = self.client.key('Recipes')
        rev = datastore.Entity(key)
        rev.update( {
            'recipe_id': recipe_id,
            'recipe_title': recipe_title,
            'recipe_url': recipe_url,
            'recipe_day': recipe_day,
            'recipe_meal': recipe_meal
            })
        self.client.put(rev)
        return True
    
    def delete(self, entity_key):
        """
        Deletes a recipe from the datastore.

        Parameters:
        ---------- 
        entity_key : str
            The key of the entity to delete.
        
        Returns:
        -------
        bool
            True if the deletion is successful.
        """
        key = self.client.key('Recipes', int(entity_key))
        self.client.delete(key)
        return True