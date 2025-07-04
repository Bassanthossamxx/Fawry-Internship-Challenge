import datetime
from models.product import Product
class Expirable(Product):
    def __init__(self, name, price, quantity, expire_date):
        super().__init__(name,price,quantity)
        self.expire_date = expire_date
    def is_expired(self):
        if self.expire_date < datetime.datetime.now():
            return True
        return False

# Testing the class:
# Create a product that expired yesterday
expired_cheese = Expirable(
    name="Old Cheese",
    price=100.75,
    quantity=10,
    expire_date=datetime.datetime(2025,7,2)
)

# Create a product that still valid
fresh_cheese = Expirable(
    name="Fresh Cheese",
    price=120,
    quantity=5,
    expire_date= datetime.datetime(2025,7,10)
)

# Print to test if working well or not
print(expired_cheese)
print("Is expired?", expired_cheese.is_expired())

print(fresh_cheese)
print("Is expired?", fresh_cheese.is_expired())