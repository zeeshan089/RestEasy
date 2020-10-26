from Abstractions import Customer
from Models.SqliteSessionandEngine import SessionAndEngine
from Models.Models import CustomerModel
from Models.UserSession import UserSession


class CustomerImplementation(Customer.Customer):

    engine = None
    session = None
    user_session = None

    def __init__(self):
        self.session_and_engine = SessionAndEngine()
        self.engine = self.session_and_engine.getEngine()
        self.session = self.session_and_engine.getSession()
        self.user_session = UserSession()

    def add_customer(self, name, username, password, level):
        #This is akin to user signup
        if not self.session.query(CustomerModel).filter_by(username=username).first():
            new_customer = CustomerModel(name=name, username=username, password=password, level=level)
            self.session.add(new_customer)
            self.session.commit()
            customer_id = new_customer.cust_id
            print("Customer added with id: " + str(customer_id))
        else:
            print("Username already exists in the database")

    def login(self, username, password):
        user_db_tuple = self.session.query(CustomerModel).filter_by(username=username).first()
        if user_db_tuple is not None and user_db_tuple.password == password:
            admin_check = False
            if int(user_db_tuple.level) == 2:
                admin_check = True

            self.user_session.login(username, admin_check)
            print(str(username) + " logged in.")
        else:
            print("Invalid username or password.")

    def logout(self):
        self.user_session.setup_or_logout()
        print("User logged out successfully!")
