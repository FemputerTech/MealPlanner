"""
This module defines the Model class, which interacts with the database to store recipes.
"""


class Model():
    """
    The Model class interacts with the database to store recipes.

    Methods:
    -------
    select_recipe(selected_week):
        Retrieves all recipes from the database for a selected week.
    
    insert_recipe(recipe_title, recipe_image, recipe_url, recipe_week_start, recipe_week_end, recipe_day, recipe_meal):
        Inserts a recipe into the database.

    delete(id):
        Deletes a recipe from the database.
    """


    def select_recipe(self, selected_week):
        """
        Retrieves all recipes from the database for a selected week.
        
        Parameters:
        ----------
        selected_week: str
            The starting date of the selected week.

        Returns:
        -------
        tuple
            A tuple containing all rows of recipes from the database for the selected week.
        """
        pass


    def insert_recipe(self, recipe_title, recipe_image, recipe_url, recipe_week_start, recipe_week_end, recipe_day, recipe_meal):
        """
        Inserts recipes into database.

        Parameters:
        ---------- 
        recipe_title : str
            The title of the recipe.
        recipe_image: str
            The URL of the recipe image.
        recipe_url: str
            The URL of the recipe.
        recipe_week_start: str
            The starting date of the week the recipe is planned for.
        recipe_week_end: str
            The end date of the week the recipe is planned for.
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