**_Resteasy Online Food Ordering CLI App_**

**Language and Tools**

Coding language: Python 3.5,
Database: Sqlite,
ORM: SQLAlchemy,
Key-Value Store: SqliteDict

**Instructions to Run**

-- Install requirements.txt

-- Add a customer(--add_customer):
Add customer takes 4 arguments, which are 'name', 'username', 'password', 'level'.
Level is 2 for admin and less than 2 for everyone else. So if you are adding an admin user, please assign him level 2.

`Ex: python3 resteasy.py --add_customer name username password level`

`$ python3 resteasy.py --add_customer john john07 john07 2`

-- Login (--login):
After you have added couple of users and admins. Please login as any user or admin.

`Ex: python3 resteasy.py --login username password`

`$ python3 resteasy.py --login john07 john07`

-- Add Vendor/Restaurant (--add_vendor):
Once you have added couple of users, now we can add few restaurants. This method takes 2 arguments; Customer_id and Restaurant name.

`Ex: python3 resteasy.py --add_vendor customer_id restaurant_name`

`$ python3 resteasy.py --add_vendor 3 thalappakatti`

-- Add dish to restaurant (--add_dish):
Now its time to add dishes to our newly added restaurant. 'add_dish' takes 5 parameters, which are 'dish_name', 'calories_per_gm', 'restaurant_id', 'available_quantity', 'unit_price'.

`Ex: python3 resteasy.py --add_dish dish_name calories_per_gm restaurant_id available_quantity unit_price`

`$ python3 resteasy.py --add_dish tk_chicken_biryani 100 4 50 200`

-- Search Dishes by name (--search_by_dish):
After you have added multiple dishes in multiple restaurants. Let's search dishes by name. A dish with same name can exist in different restaurants.
This takes 2 parameters, dish name and 'sort result by'. The results are sorted in ascending order of price by default. Specify, if you want to sort them by descending order of price. 

`Ex: python3 resteasy.py --search_by_dish dish_name result_sort_by`

`$ python3 resteasy.py --search_by_dish tk_mutton_biryani descending`

-- Search Dishes by Restaurant (--search_by_restaurant):
You can also search for food by restaurant. This method that 2 arguments, restaurant_id and 'result_sort_by'.

`Ex: python3 resteasy.py --search_by_restaurant restaurant_id result_sort_by`

`$ python3 resteasy.py --search_by_restaurant 1 descending`

-- Place an order (--place_order):
Placing an order requires 'atleast' one dish and can take any number of dishes for order from different restaurants.
Your individual dish order **should be like 'dish_name,restaurant_name,quantity' without spaces**. And you can place as many dishes as you like in a single order from different restaurants.

`Ex: python3 resteasy.py --place_order dish_name,restaurant_name,quantity dish_name,restaurant_name,quantity`

`$ python3 resteasy.py --place_order McChicken,McDonalds,1 tk_mutton_biryani,thalappakatti,1`

-- Check orders by a customer(--get_all_orders_by_customer):
You can fetch the entire list of all the orders placed by a customer. This only takes username as a parameter.

`Ex: python3 resteasy.py --get_all_orders_by_customer username`

`$ python3 resteasy.py --get_all_orders_by_customer john07`

-- Fetch all orders till date (--get_all_orders)(Admin Only):
You can fetch all the orders received till date with their item and amount details. Only admin can call this functionality. You should be logged in as admin to call this.
This method only requires one parameter, admin name.

`Ex: python3 resteasy.py --get_all_orders admin_name`

`$ python3 resteasy.py --get_all_orders john07`

-- Fetch list of all restaurants (--get_all_vendors):
You can fetch the list of all restaurants. This only requires one parameter, username.

`Ex: python3 resteasy.py --get_all_vendors username`

`$ python3 resteasy.py --get_all_vendors xyz`

-- logout (--logout):
Logging out of application. Takes a single parameter username as input.

`Ex: python3 resteasy.py --logout username`

`$ python3 resteasy.py --logout john07`