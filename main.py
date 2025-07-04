import datetime
from models.product import Product
from models.expirable import Expirable
from models.shippable import Shippable
from models.customer import Customer
from models.cart import Cart
from services.checkout import checkout


#Custom Product Types

class Cheese(Expirable, Shippable):
    def __init__(self, name, price, quantity, expire_date, weight):
        Expirable.__init__(self, name, price, quantity, expire_date)
        Shippable.__init__(self, weight)


class TV(Product, Shippable):
    def __init__(self, name, price, quantity, weight):
        Product.__init__(self, name, price, quantity)
        Shippable.__init__(self, weight)


class ScratchCard(Product):
    # Not expirable, not shippable
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


class Biscuits(Expirable, Shippable):
    def __init__(self, name, price, quantity, expire_date, weight):
        Expirable.__init__(self, name, price, quantity, expire_date)
        Shippable.__init__(self, weight)


# Testing Scenario

def main():
    # Create a customer
    customer = Customer(name="Bassant", balance=1000)

    # Create products
    cheese = Cheese("Cheese", 100, 5, datetime.datetime(2025, 8, 1), 0.4)
    tv = TV("TV", 300, 2, 5.0)
    scratch_card = ScratchCard("Scratch Card", 50, 10)
    biscuits = Biscuits("Biscuits", 150, 1, datetime.datetime(2025, 7, 10), 0.7)

    # Create a cart
    cart = Cart()

    # Add items to the cart
    cart.add_item(cheese, 2)
    cart.add_item(tv, 1)
    cart.add_item(scratch_card, 1)
    cart.add_item(biscuits, 1)

    # Checkout
    print("\n--- Starting Checkout ---\n")
    try:
        checkout(customer, cart)
    except ValueError as e:
        print(f" Error during checkout: {e}")


if __name__ == "__main__":
    main()
