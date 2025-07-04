import datetime
from models.product import Product
from models.expirable import Expirable
from models.shippable import Shippable
from models.customer import Customer
from models.cart import Cart
from services.checkout import checkout

# Custom Product Types

#1- Expirable & Shippable Product
class ExpirableShippableProduct(Expirable, Shippable):
    def __init__(self, name, price, quantity, expire_date, weight):
        Expirable.__init__(self, name, price, quantity, expire_date)
        Shippable.__init__(self, weight)
#2- Shippable Product
class ShippableProduct(Product, Shippable):
    def __init__(self, name, price, quantity, weight):
        Product.__init__(self, name, price, quantity)
        Shippable.__init__(self, weight)

# === Test Main Function

def main():
 # Success Scenario
    print("\n--- Scenario : Success Checkout ---")
    customer = Customer(name="Bassant", balance=1000)
    cheese = ExpirableShippableProduct("Cheese", 100, 5, datetime.datetime(2025, 8, 1), 0.4)
    tv = ShippableProduct("TV", 300, 2, 5.0)
    scratch_card = Product("Scratch Card", 50, 10)
    biscuits = ExpirableShippableProduct("Biscuits", 150, 1, datetime.datetime(2025, 7, 10), 0.7)

    cart = Cart()
    cart.add_item(cheese, 2)
    cart.add_item(tv, 1)
    cart.add_item(scratch_card, 1)
    cart.add_item(biscuits, 1)

    try:
        checkout(customer, cart)
    except ValueError as e:
        print(f" Error during checkout: {e}")


    print("-------------------------------------------------")
    print("---- Edge Cases : ----")

    # === Edge Case 1: Empty Cart ===
    print("\n 1- Edge Case: Empty Cart")
    cart1 = Cart()
    try:
        checkout(customer, cart1)
    except ValueError as e:
        print(f" ERROR : empty cart: {e}")

    # === Edge Case 2: Expired Product ===
    print("\n 2- Edge Case: Expired Product ")
    expired_biscuits = ExpirableShippableProduct("Old Biscuits", 120, 3, datetime.datetime(2020, 1, 1), 0.3)
    cart2 = Cart()
    cart2.add_item(expired_biscuits, 1)
    try:
        checkout(customer, cart2)
    except ValueError as e:
        print(f" ERROR : expired product: {e}")

    # === Edge Case 3: Invalid Balance ===
    print("\n3- Edge Case: Invalid Balance ")
    poor_customer = Customer(name="bassant", balance=100)
    cart3 = Cart()
    cart3.add_item(tv, 1)  # TV = 300
    try:
        checkout(poor_customer, cart3)
    except ValueError as e:
        print(f"ERROR : invalid balance: {e}")

    # === Edge Case 4: Quantity Requested > Available ===
    print("\n 4- Edge Case: Quantity > Available ")
    cart4 = Cart()
    try:
        cart4.add_item(cheese, 10)  # cheese only has 3 left
    except ValueError as e:
        print(f" ERROR : invalid quantity: {e}")

if __name__ == "__main__":
    main()
