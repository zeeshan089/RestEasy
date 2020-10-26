from Abstractions import Food
from Models.SqliteSessionandEngine import SessionAndEngine
from Models.Models import VendorModel, CustomerModel, FoodModel
from Models.UserSession import UserSession
from sqlalchemy import desc


class FoodImplementation(Food.Food):

    engine = None
    session = None
    user_session = None

    def __init__(self):
        self.session_and_engine = SessionAndEngine()
        self.engine = self.session_and_engine.getEngine()
        self.session = self.session_and_engine.getSession()
        self.user_session = UserSession()

    def add_dish(self, dish_name, calories_per_gm, restaurant_id, available_quantity, unit_price):
        if self.user_session.check_login():
            if self.session.query(VendorModel).filter_by(vendor_id=restaurant_id).first():
                new_dish = FoodModel(vendor_id=restaurant_id, dish_name=dish_name, calories_per_gm=calories_per_gm, available_quantity=available_quantity, unit_price=unit_price)
                self.session.add(new_dish)
                self.session.commit()
                print(dish_name + " added in restaurant " + str(restaurant_id))
            else:
                print("Invalid restaurant ID.")
        else:
            return "Please signup or login first."

    def get_dish_by_name(self, dish_name, sort_by = 'ascending'):
        if self.user_session.check_login():
            dishes_rs = None
            if sort_by == 'descending':
                dishes_rs = self.session.query(FoodModel).filter_by(dish_name=dish_name).order_by(desc(FoodModel.unit_price))
            else:
                dishes_rs = self.session.query(FoodModel).filter_by(dish_name=dish_name).order_by(FoodModel.unit_price)

            for row in dishes_rs:
                print(row)
        else:
            return "Please signup or login first."

    def get_dishes_by_restaurant(self, restaurant_id, sort_by='ascending'):
        if self.user_session.check_login():
            dishes_rs = None
            if sort_by == 'descending':
                dishes_rs = self.session.query(FoodModel).filter_by(vendor_id=restaurant_id).order_by(desc(FoodModel.unit_price))
            else:
                dishes_rs = self.session.query(FoodModel).filter_by(vendor_id=restaurant_id).order_by(FoodModel.unit_price)

            for row in dishes_rs:
                print(row)
        else:
            return "Please signup or login first."
