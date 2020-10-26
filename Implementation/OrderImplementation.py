from Abstractions import Order
from Models.SqliteSessionandEngine import SessionAndEngine
from Models.Models import VendorModel, CustomerModel, FoodModel, OrdersModel, OrderItemsModel
from Models.UserSession import UserSession
import datetime


class OrderImplementation(Order.Order):

    engine = None
    session = None
    user_session = None

    def __init__(self):
        self.session_and_engine = SessionAndEngine()
        self.engine = self.session_and_engine.getEngine()
        self.session = self.session_and_engine.getSession()
        self.user_session = UserSession()

    def place_order(self, customer_id, total_amount, date):
        new_order = OrdersModel(cust_id=customer_id, total_amount=total_amount, date=date)
        self.session.add(new_order)
        self.session.commit()
        order_number = new_order.order_id
        return order_number

    def add_order_items(self, order_id, food_id, quantity, amount):
        new_item = OrderItemsModel(order_id=order_id, food_id=food_id, quantity=quantity, amount=amount)
        self.session.add(new_item)
        self.session.commit()
        return True

    def compose_order(self, order_list):
        if self.user_session.check_login():
            amount = 0
            order_items = []
            username = self.user_session.loggedIn_User()
            customer_row = self.session.query(CustomerModel).filter_by(username=username).first()
            customer_id = customer_row.cust_id
            for dish_name, restaurant_name, quantity in order_list:
                restaurant = self.session.query(VendorModel).filter_by(restaurant_name=restaurant_name).first()
                food_row = self.session.query(FoodModel).filter_by(dish_name=dish_name, vendor_id=restaurant.vendor_id).first()
                if food_row:
                    orderItem_amount = int(quantity) * int(food_row.unit_price)
                    orderItem_tuple = (food_row.food_id, quantity, orderItem_amount)
                    order_items.append(orderItem_tuple)
                    amount += orderItem_amount

            order_number = self.place_order(customer_id, amount, datetime.date.today())

            for food_id, quantity, item_amount in order_items:
                self.add_order_items(order_number, food_id, quantity, item_amount)

            print("Order Placed")
        else:
            print("Please signup or login first.")

    def get_all_orders_by_customer(self, username):
        customer_row = self.session.query(CustomerModel).filter_by(username=username).first()
        customer_name = customer_row.name
        customer_id = customer_row.cust_id

        order_rows = self.session.query(OrdersModel).filter_by(cust_id=customer_id)
        for row in order_rows:
            order_number = row.order_id
            order_amount = row.total_amount
            order_date = row.date

            ##Print the order high level data first below
            print("-------Order Start---------------")
            print("Customer Name: " + customer_name)
            print("Order Number: " + str(order_number))
            print("Order Date: " + str(order_date))
            print("Total Order Value: " + str(order_amount))
            print("Order Items: ")

            order_items = self.session.query(OrderItemsModel).filter_by(order_id=order_number)

            for item_row in order_items:
                food_row = self.session.query(FoodModel).filter_by(food_id=item_row.food_id).first()
                dish_name = food_row.dish_name
                unit_price = food_row.unit_price
                restaurant_row = self.session.query(VendorModel).filter_by(vendor_id=food_row.vendor_id).first()
                restaurant_name = restaurant_row.restaurant_name
                item_quantity = item_row.quantity
                item_amount = item_row.amount

                print("Dish Name: " + str(dish_name) + "|" + " Restaurant Name: " + str(restaurant_name) + "|" + " Quantity: " + str(item_quantity) + "|" + " Unit Price: " + str(unit_price) + "|" + " Amount: " + str(item_amount))

            print("-------Order End---------------")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def get_all_orders(self):
        if self.user_session.check_admin():
            for row in self.session.query(OrdersModel).all():
                order_number = row.order_id
                order_amount = row.total_amount
                order_date = row.date

                customer_row = self.session.query(CustomerModel).filter_by(cust_id=row.cust_id).first()
                customer_name = customer_row.name

                # Print the order high level data first below
                print("-------Order Start---------------")
                print("Customer Name: " + customer_name)
                print("Order Number: " + str(order_number))
                print("Order Date: " + str(order_date))
                print("Total Order Value: " + str(order_amount))
                print("Order Items: ")

                order_items = self.session.query(OrderItemsModel).filter_by(order_id=order_number)

                for item_row in order_items:
                    food_row = self.session.query(FoodModel).filter_by(food_id=item_row.food_id).first()
                    dish_name = food_row.dish_name
                    unit_price = food_row.unit_price
                    restaurant_row = self.session.query(VendorModel).filter_by(vendor_id=food_row.vendor_id).first()
                    restaurant_name = restaurant_row.restaurant_name
                    item_quantity = item_row.quantity
                    item_amount = item_row.amount

                    print("Dish Name: " + str(dish_name) + " Restaurant Name: " + str(restaurant_name) + " Quantity: " + str(item_quantity) + " Unit Price: " + str(unit_price) + " Amount: " + str(item_amount))

                print("-------Order End---------------")
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        else:
            print("Only Admin can see all orders.")
