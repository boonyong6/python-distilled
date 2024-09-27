# Example 1: Instance caching using __new__().
class Date:
    year: int
    month: int
    day: int

    _cache = {}

    # `cls` can be other than `Date`. So, this is not a class method.
    def __new__(cls, year, month, day):
        self = Date._cache.get((year, month, day))
        if not self:
            # 1. Create an instance using object.__new__().
            self = super().__new__(cls)
            # 2. Initialize the instance.
            self.year = year
            self.month = month
            self.day = day

            Date._cache[year, month, day] = self

        return self

    # Every call to Date() calls __init__().
    # This method is empty because initialization is already done in __new__().
    def __init__(self, year, month, day):
        pass


d = Date(2012, 12, 21)
e = Date(2012, 12, 21)
assert d is e  # Same object


# Example 2: Proper resource cleanup
class Resource:
    def close(self):
        print(f"Invoked {self.close.__qualname__}().")

    @classmethod
    def open(cls):
        print(f"Invoked {cls.open.__qualname__}().")
        return Resource()


class SomeClass:
    def __init__(self):
        self.resource = Resource.open()
        self.disposed = False

    # Calls the resource cleanup handler
    #   when the instance is about to be garbage collected 
    #   (unpredictable timing).
    def __del__(self):
        print(f"Invoked {self.__del__.__qualname__}()")

        if self.disposed:
            print(f"{self} has been disposed.")
            return

        self.close()

    # Resource cleanup handler.
    def close(self):
        print(f"Invoked {self.close.__qualname__}()")
        self.resource.close()
        self.disposed = True

    def __enter__(self):
        return self

    # Calls the resource cleanup handler
    #   at the end of the "with" statement (end of context).
    def __exit__(self, ty, val, tb):
        print(f"Invoked {self.__exit__.__qualname__}()")
        self.close()


# Closed via __del__()
s = SomeClass()
del s
print()

# Explicit close
s = SomeClass()
s.close()

# Closed at the end of a context block.
with SomeClass() as s:
    ...
