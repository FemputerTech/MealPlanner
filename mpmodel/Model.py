"""
This module defines the Model class, which interacts with the database to store recipes.
"""


class Model():
    """
    The Model class interacts with the database to store recipes.

    Methods:
    -------
    select():
        Retrieves all recipes from the database.
    
    insert_recipe(recipe_id, recipe_title, recipe_url, recipe_day, recipe_meal):
        Inserts a recipe into the database.

    delete(id):
        Deletes a recipe from the database.
    """


    def select(self):
        """
        Retrieves all recipes from the database.
        
        Returns:
        -------
        tuple
            A tuple containing all rows of recipes from the database.
        """
        pass


    def insert_recipe(self, recipe_id, recipe_title, recipe_url, recipe_day, recipe_meal):
        """
        Inserts recipes into database.

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
        None
        """
        pass

    def delete(self, id):
        """
        Deletes a recipe from the database.

        Parameters:
        ---------- 
        id : str
            The key of the entity to delete.
        """
        pass