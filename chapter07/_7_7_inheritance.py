from account import Account

# Use case 1: To extend an existing class with new methods.
class MyAccount(Account):
    # New method
    def panic(self):
        self.withdraw(self.balance)

a = MyAccount("Guido", 1000.0)
a.withdraw(23.0)
print(a.balance)

a.panic()
print(a.balance)


# Use case 2: To redefine an existing method 
#   but also call the original implementation (using super()).
# Use case 3: To add additional attributes.
import random

class EvilAccount(Account):
    # Redefine __init__() to add additional attribute(s).
    def __init__(self, owner, balance, factor):
        super().__init__(owner, balance)  # <--
        self.factor = factor

    # Existing method
    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.factor * super().inquiry()  # <--
        else:
            return super().inquiry()  # <--

a = EvilAccount("Guido", 1000.0, 1.10)
a.deposit(10.0)
available = a.inquiry()
print(available)

print(repr(a))
