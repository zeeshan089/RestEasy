class Customer:

    def add_customer(self, username, name, password, level):
        """This is the abstract method to add a customer. level field determines if he is a user, vendor or admin."""
        pass

    def login(self, username, password):
        """This method will be used to login an existing customer."""
        pass

    def logout(self):
        """This method will be used to logout an existing customer."""
        pass

    def update_customer_name_or_password(self, username, name, password):
        """This is the abstract method to update the customer's name or password or both. level field determines if he is a user, vendor or admin."""
        pass

    # The following two methods can only be called by Admin
    def remove_customer(self, username):
        """This is the abstract method to remove a customer. Only admin can remove a user."""
        pass

    def upgrade_customer(self, username, level):
        """This is the abstract method to upgrade the customer level. Only admin can upgrade any user."""
        pass
