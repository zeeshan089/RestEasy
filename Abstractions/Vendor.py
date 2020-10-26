class Vendor:

    def add_vendor(self, customer_id, restaurant_name):
        """This is the abstract method to add a vendor."""
        pass

    def get_all_vendors(self):
        """This method will fetch all the vendors list"""
        pass

    def update_restaurant_name(self, customer_id, restaurant_id, new_restaurant_name):
        """This is the abstract method to update the customer's name or password or both. level field determines if he is a user, vendor or admin."""
        pass

    # The following methods can only be called by Admin
    def remove_vendor(self, restaurant_id):
        """This is the abstract method to remove a customer. Only admin can remove a user."""
        pass

