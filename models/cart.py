from models.shippable import Shippable

class Cart:
    def __init__(self):
        self.items = []  # List of (product, quantity)

    def is_empty(self):
        #check if empty
        return len(self.items) == 0

    def get_subtotal(self):
        #calc subtotal
        return sum(product.price * quantity for product, quantity in self.items)

    def add_item(self, product, quantity):
        # Check if enough quantity available
        if quantity > product.quantity:
            print(f" Not enough stock for {product.name}. Only {product.quantity} left.")
            return

        # Check if product is expired "only if it is expirable product"
        try:
            if product.is_expired():
                print(f" {product.name} is expired. Cannot add to cart.")
                return
        except AttributeError:
            pass  # If is_expired doesn't exist, ignore

        # add to cart
        self.items.append((product, quantity))
        product.quantity -= quantity
        print(f" Added {quantity}x {product.name} to cart.")

    def get_shippable_items(self):
        shippables_items = []
        for product, quantity in self.items:
            if isinstance(product, Shippable):
                for _ in range(quantity):
                    shippables_items.append(product)
        return shippables_items