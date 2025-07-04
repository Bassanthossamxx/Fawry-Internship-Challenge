class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if amount > self.balance:
            raise ValueError(f"{self.name} has invalid balance. Needed: {amount}, Available: {self.balance}")
        self.balance -= amount
        print(f" {self.name} paid {amount} EGP. Remaining balance: {self.balance} EGP.")

    def __str__(self):
        return f"Customer: {self.name}, Balance: {self.balance} EGP"
