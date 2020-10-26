class Order:

    def place_order(self, customer_id, total_amount, date_time):
        """This method will be used to place the order"""
        pass

    def add_order_items(self, order_id, food_id, quantity, amount):
        """This method will be used to add individual items to the order."""
        pass

    def compose_order(self, order_list, customer_id):
        """This method will be used to compose and calculate the total order before making a db entry."""
        pass

    def get_all_orders_by_customer(self, customer_id):
        """This method will be used to fetch all orders by a customer."""
        pass

    def get_all_orders(self):
        """Only admin can view all the orders placed."""
        pass

    def update_order_items(self, order_id, food_id, quantity):
        """This method will be used to update individual items to the order. This will only update the quantity."""
        pass

    def remove_order_items(self, order_id, food_id):
        """This method will be used to remove individual items to the order."""
        pass

    def cancel_order(self, order_id):
        """This method will be used to cancel the order."""
        pass