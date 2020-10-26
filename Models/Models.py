from sqlalchemy import Integer, Column, String, ForeignKey, Date
from Models.SqliteSessionandEngine import SessionAndEngine
from sqlalchemy.ext.declarative import declarative_base


session_and_engine = SessionAndEngine()

Base = declarative_base()
engine = session_and_engine.getEngine()


class CustomerModel(Base):
    __tablename__ = 'customer'
    cust_id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    level = Column(Integer)

    def __repr__(self):
        return "<Customer(name='%s', username='%s', level='%s')>" % (
            self.name, self.username, str(self.level))


class VendorModel(Base):
    __tablename__ = 'vendor'
    vendor_id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey("customer.cust_id"))
    restaurant_name = Column(String)

    def __repr__(self):
        return "<Vendor(vendor_id='%s', restaurant_name='%s')>" % (str(self.vendor_id), self.restaurant_name)


class FoodModel(Base):
    __tablename__ = 'food'
    food_id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey("vendor.vendor_id"))
    dish_name = Column(String)
    calories_per_gm = Column(Integer)
    available_quantity = Column(Integer)
    unit_price = Column(Integer)

    def __repr__(self):
        return "<Food(food_id='%s', vendor_id='%s', dish_name='%s', calories_per_gm='%s', available_quantity='%s', unit_price='%s')>" % (str(self.food_id), str(self.vendor_id), self.dish_name, self.calories_per_gm, str(self.available_quantity), str(self.unit_price))


class OrdersModel(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey("customer.cust_id"))
    total_amount = Column(Integer)
    date = Column(Date)

    def __repr__(self):
        return "<Orders(order_id='%s', customer_id='%s', total_order_amount='%s', order_date='%s')>" % (str(self.order_id), str(self.cust_id), str(self.total_amount), str(self.date))


class OrderItemsModel(Base):
    __tablename__ = 'orderItems'
    item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    food_id = Column(Integer, ForeignKey("food.food_id"))
    quantity = Column(Integer)
    amount = Column(Integer)

    def __repr__(self):
        return "<OrderItems(item_id='%s', order_id='%s', food_id='%s', quantity='%s', quantity='%s')>" % (str(self.item_id), str(self.order_id), str(self.food_id), str(self.quantity), str(self.amount))


Base.metadata.create_all(engine)
