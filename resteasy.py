#!/usr/bin/env python
import argparse
import Driver

class RestEasy:

    def __init__(self):

        # create parser object
        parser = argparse.ArgumentParser(description="A CLI based food ordering app")

        # defining arguments for parser object

        parser.add_argument("--add_customer", type=str, nargs=4,
                            metavar=("name", "username", "password", "level"), default=None,
                            help="Provide name, username, password and level of new customer")

        parser.add_argument("--login", type=str, nargs=2,
                            metavar=("username", "password"), default=None,
                            help="Provide username and password to login.")

        parser.add_argument("--add_vendor", type=str, nargs=2,
                            metavar=("customer_id", "restaurant_name"), default=None,
                            help="Provide a valid customer_id and restaurant name.")

        parser.add_argument("--add_dish", type=str, nargs=5,
                            metavar=("dish_name", "calories_per_gm", "restaurant_id", "available_quantity", "unit_price"),
                            help="Provide dish name, calories, restaurant_id, available quantity, unit price")

        parser.add_argument("--search_by_dish", type=str, nargs=2,
                            metavar=("dish name", "sort result by"),
                            help="provide a dish name and 'sort result by' arguments")

        parser.add_argument("--search_by_restaurant", type=str, nargs=2,
                            metavar=("restaurant id", "sort result by"),
                            help="provide a restaurant name and 'sort result by' arguments")

        parser.add_argument('--place_order', type=self.pair, nargs='+')

        parser.add_argument("--get_all_orders_by_customer", type=str, nargs=1,
                            metavar=("username"), default=None,
                            help="Provide username to fetch all orders")

        parser.add_argument("--get_all_orders", type=str, nargs=1, metavar=("username"), default=None, help="fetch the list of all orders till date. Can only be called by admin.")

        parser.add_argument("--get_all_vendors", type=str, nargs=1, metavar=("username"), default=None, help="fetch the list of all vendors")

        parser.add_argument("--logout", type=str, nargs=1, metavar=("username"), default=None, help="logout from app")

        # parse the arguments from standard input
        args = parser.parse_args()

        # calling functions depending on type of argument

        if args.add_customer != None:
            driver.add_customer(args)
        elif args.login != None:
            driver.login(args)
        elif args.add_vendor != None:
            driver.add_vendor(args)
        elif args.add_dish != None:
            driver.add_dish(args)
        elif args.search_by_dish != None:
            driver.search_by_dish(args)
        elif args.search_by_restaurant != None:
            driver.search_by_restaurant(args)
        elif args.place_order != None:
            driver.place_order(args)
        elif args.get_all_orders_by_customer != None:
            driver.get_all_orders_by_customer(args)
        elif args.get_all_orders != None:
            driver.get_all_orders(args)
        elif args.get_all_vendors != None:
            driver.get_all_vendors(args)
        elif args.logout != None:
            driver.logout(args)


    def pair(self, arg):
        return [str(x) for x in arg.split(',')]


driver = Driver.Driver()
RestEasy()