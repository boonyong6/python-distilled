# Example:
import types


# Some methods (not in a class)
def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance


def deposit(self, amount):
    self.balance += amount


def withdraw(self, amount):
    self.balance -= amount


methods = {"__init__": __init__, "deposit": deposit, "withdraw": withdraw}

Account = types.new_class("Account", (), exec_body=lambda ns: ns.update(methods))

a = Account("Guido", 1000.0)
a.deposit(50)
a.withdraw(25)
print(vars(a))

# Example: To create classes from data structures.
# * Classes (in _7_28_descriptors.py) to recreate dynamically.
# class Integer(Typed):
#     expected_type = int

# class Float(Typed):
#     expected_type = float

# class String(Typed):
#     expected_type = str

# * To create the above classes dynamically.
from _7_28_descriptors import Typed

typed_classes = [
    ("Integer", int),
    ("Float", float),
    ("String", str),
]


def create_class(name, ty):
    return types.new_class(
        name, (Typed,), exec_body=lambda ns: ns.update(expected_type=ty)
    )


globals().update((name, create_class(name, ty)) for name, ty in typed_classes)

print(globals())
