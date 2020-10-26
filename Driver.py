import Models.Models
from Implementation import CustomerImplementation, VendorImplementation, FoodImplementation, OrderImplementation


class Driver:

    def __init__(self):
        self.customer = CustomerImplementation.CustomerImplementation()
        self.vendor = VendorImplementation.VendorImplementation()
        self.food = FoodImplementation.FoodImplementation()
        self.order = OrderImplementation.OrderImplementation()

    def add_customer(self, args):
        name = str(args.add_customer[0])
        username = str(args.add_customer[1])
        password = str(args.add_customer[2])
        level = int(args.add_customer[3])
        self.customer.add_customer(name, username, password, level)

    def login(self, args):
        username = str(args.login[0])
        password = str(args.login[1])
        self.customer.login(username, password)

    def add_vendor(self, args):
        customer_id = int(args.add_vendor[0])
        restaurant_name = str(args.add_vendor[1])
        self.vendor.add_vendor(customer_id, restaurant_name)

    def add_dish(self, args):
        dish_name = str(args.add_dish[0])
        calories_per_gm = int(args.add_dish[1])
        restaurant_id = int(args.add_dish[2])
        available_quantity = int(args.add_dish[3])
        unit_price = int(args.add_dish[4])
        self.food.add_dish(dish_name, calories_per_gm, restaurant_id, available_quantity, unit_price)

    def search_by_dish(self, args):
        dish_name = str(args.search_by_dish[0])
        sort_by = str(args.search_by_dish[1])
        self.food.get_dish_by_name(dish_name, sort_by)

    def search_by_restaurant(self, args):
        restaurant_id = int(args.search_by_restaurant[0])
        sort_by = str(args.search_by_restaurant[1])
        self.food.get_dishes_by_restaurant(restaurant_id, sort_by)

    def place_order(self, args):
        order_list = args.place_order
        print(order_list)
        self.order.compose_order(order_list)

    def get_all_orders_by_customer(self, args):
        username = args.get_all_orders_by_customer[0]
        self.order.get_all_orders_by_customer(username)

    def get_all_orders(self, args):
        self.order.get_all_orders()

    def get_all_vendors(self, args):
        self.vendor.get_all_vendors()

    def logout(self, args):
        self.customer.logout()


