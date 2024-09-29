from account import Account

# When a class is defined, it becomes an object.
print(isinstance(Account, object))

# `type` is the metaclass that create class objects.
# So, `Account` is an instance of `type`.
print(Account.__class__)


# Example 1: User-defined metaclass
class mytype(type):
    # Creates the class namespace.
    @classmethod
    def __prepare__(metacls, cls_name, bases):
        print("Preparing:", cls_name, bases)
        return super().__prepare__(cls_name, bases)
    
    # Creates the class instance after body has executed.
    def __new__(metacls, cls_name, bases, namespace):
        print("Creating:", cls_name, bases, namespace)
        return super().__new__(metacls, cls_name, bases, namespace)
    
    # Initialize the class instance.
    def __init__(cls, cls_name, bases, namespace):
        print("Initializing:", cls_name, bases, namespace)
        super().__init__(cls_name, bases, namespace)

    # Creates new instances of the class.
    def __call__(cls, *args, **kwargs):
        print("Creating instance:", args, kwargs)
        return super().__call__(*args, **kwargs)

class Base(metaclass=mytype):
    pass

b = Base()


# * Use case: Rewrite the contents of the class namespace.
# NOTE: Certain features of classes are established at definition time and 
#   can't be modified later, such as __slots__.
# Example 2: A metaclass that automatically sets the __slots__ attribute 
#   based on the calling signature of the __init__().
import inspect

class SlotMeta(type):
    def __new__(metacls, cls_name, bases, namespace):
        if "__init__" in namespace:
            sig = inspect.signature(namespace["__init__"])
            __slots__ = tuple(sig.parameters)[1:]
        else:
            __slots__ = ()
        
        namespace["__slots__"] = __slots__
        return super().__new__(metacls, cls_name, bases, namespace)

class BaseSlot(metaclass=SlotMeta):
    pass

class Point(BaseSlot):
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(vars(Point))
