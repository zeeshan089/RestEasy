from Abstractions import Vendor
from Models.SqliteSessionandEngine import SessionAndEngine
from Models.Models import VendorModel, CustomerModel
from Models.UserSession import UserSession


class VendorImplementation(Vendor.Vendor):

    engine = None
    session = None
    user_session = None

    def __init__(self):
        self.session_and_engine = SessionAndEngine()
        self.engine = self.session_and_engine.getEngine()
        self.session = self.session_and_engine.getSession()
        self.user_session = UserSession()

    def add_vendor(self, customer_id, restaurant_name):
        """Customer id should be in db while restaurant name shouldn't be"""
        if self.user_session.check_login():
            if self.session.query(CustomerModel).filter_by(cust_id=customer_id).first() and not self.session.query(VendorModel).filter_by(restaurant_name=restaurant_name).first():
                new_vendor = VendorModel(cust_id=customer_id, restaurant_name=restaurant_name)
                self.session.add(new_vendor)
                self.session.commit()
                restaurant_id = new_vendor.vendor_id
                print("Vendor added successfully with id: " + str(restaurant_id))
            else:
                print("Invalid Customer id or Restaurant name already exists.")
        else:
            print("Please signup or login first.")

    def get_all_vendors(self):
        """This method will fetch all the vendors list"""
        if self.user_session.check_login():
            for row in self.session.query(VendorModel).all():
                print(row)
        else:
            return "Please signup or login first."
