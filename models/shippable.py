from models.product import Product
#mixin class
class Shippable:
    def __init__(self, weight):
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

"""
#test The Shippable Class :
class TV(Product, Shippable):
    def __init__(self, name, price, quantity, weight):
        Product.__init__(self, name, price, quantity)
        Shippable.__init__(self, weight)
#obj to test it
tv = TV("Samsung TV", 10000, 3, 7.5)
print(tv.get_name())
print(tv.get_weight())
"""


