# Example: Reimplement __setattr__
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __setattr__(self, name, value):
        if name not in {"owner", "balance"}:
            raise AttributeError(f"No attribute {name}")
        super().__setattr__(name, value)


acct = Account("Guido", 1000.0)
acct.balance = 940.25
# acct.amount = 540.2  # Raise AttributeError: No attribute amount


# Modifications to an instance are reflected in the __dict__ attribute.
acct = Account("Guido", 1000.0)
print(acct.__dict__)

acct.owner = "Ben"
print(acct.__dict__)

# Modifications to __dict__ are reflected in the attributes.
acct.__dict__["balance"] = 666
print(acct.balance)


# An instance `acct` is linked back to its class.
print(acct.__class__)


# A class is just a thin layer over a dictionary.
print(Account.__dict__)


# A class is linked to its base classes.
print(Account.__bases__)
