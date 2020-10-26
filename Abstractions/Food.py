class Food:

    def add_dish(self, dish_name, calories_per_gm, restaurant_id, available_quantity, unit_price):
        """This abstract method will be used to add dishes for individual restaurants."""
        pass

    def get_dish_by_name(self, dish_name, sort_by='ascending'):
        """This abstract method will be used to search for dishes by name."""
        pass

    def get_dishes_by_restaurant(self, restaurant_id, sort_by='ascending'):
        """This abstract method will be used to get all dishes of a restaurant."""
        pass

    def update_dish(self, dish_id, dish_name, calories_per_gm, restaurant_id, available_quantity, unit_price):
        """This abstract method will be used to update dishes for individual restaurants."""
        pass

    def remove_dish(self, food_id, restaurant_id):
        """This abstract method will be used to remove dishes for individual restaurants."""
        pass
