# Example: Descriptor that perform type checking.
class Typed:
    expected_type = object

    # Invoked after a class has been defined, 
    #   but before any instances have been created.
    def __set_name__(self, cls, name):
        self.key = name

    def __get__(self, instance, cls):
        if instance:
            return instance.__dict__[self.key]
        # When __get__() is invoked at the class level.
        else:
            return self

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")

        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute.")


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Account:
    # Instantiate descriptors at the class-level.
    owner = String()
    balance = Float()

    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance


a = Account("Guido", 1000.0)
b = a.owner         # Calls Account.owner.__get__(a, Account)
a.owner = "Eva"     # Calls Account.owner.__set__(a, "Eva")
# del a.owner         # Calls Account.owner.__delete__(a)


# If `__get__()` is invoked at the class level (e.g. `Account`), 
#   the `instance` argument is `None`.
print(Account.balance) # type: ignore


# Example: Method descriptors - @classmethod, @staticmethod
# ! skeleton implementation
import types

class classmethod:
    def __init__(self, func):
        self.__func__ = func

    # Return a bound method with cls as first argument
    def __get__(self, instance, cls):
        return types.MethodType(self.__func__, cls)

class staticmethod:
    def __init__(self, func):
        self.__func__ = func
    
    # Return the bare function
    def __get__(self, instance, cls):
        return self.__func__


# Example: Lazy evaluation of attributes.
class Lazy:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, cls, name):
        self.key = name
    
    def __get__(self, instance, cls):
        if instance:
            value = self.func(instance)
            instance.__dict__[self.key] = value
            return value
        else:
            return self


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    area = Lazy(lambda self: self.width * self.height)
    perimeter = Lazy(lambda self: 2 * self.width + 2 * self.height)

r = Rectangle(3, 4)
print(r.__dict__)   # {'width': 3, 'height': 4}
print(r.area)       # 12
print(r.perimeter)  # 14
print(r.__dict__)   # {'width': 3, 'height': 4, 'area': 12, 'perimeter': 14}

# `area` is in `r.__dict__`, no call to `__get__()` (method descriptor).
print(r.area)
