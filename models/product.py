class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    # __str__ method to return a string representation
    def __str__(self):
        message = f'Name : {self.name} , Price : {self.price} EGP , Quantity : {self.quantity}'
        return message

#test the Product class:
scratch_cards = Product("scratch cards", 50, 4) #inital obj from the base class
#Print the Product object
print(scratch_cards)