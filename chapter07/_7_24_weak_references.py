from account import Account
import weakref

a = Account("Guido", 1000.0)

# Referencing `a`` with weakref doesn't increase the reference count.
a_ref = weakref.ref(a)
print(a_ref)    # <weakref at 0x0000017C6ED058A0; to 'Account' at 0x0000017C6EB77D60>
print(a_ref())  # Account('Guido', 1000.0)

del a
print(a_ref())  # None
print(a_ref)    # <weakref at 0x0000017C6ED058A0; dead>

print()


# Example: Automatically removes objects from the cache
#   when no more references exist.
class Date:
    year: int
    month: int
    day: int

    _cache = {}

    # `cls` can be other than `Date`. So, this is not a class method.
    def __new__(cls, year, month, day):
        self_ref = Date._cache.get((year, month, day))
        if not self_ref:
            # 1. Create an instance using object.__new__().
            self = super().__new__(cls)
            # 2. Initialize the instance.
            self.year = year
            self.month = month
            self.day = day

            Date._cache[year, month, day] = weakref.ref(self)
        else:
            self = self_ref()
        return self

    # Every call to Date() calls __init__().
    # This method is empty because initialization is already done in __new__().
    def __init__(self, year, month, day):
        pass

    def __del__(self):
        del Date._cache[self.year, self.month, self.day]


print(Date._cache)

a = Date(2012, 12, 21)
print(Date._cache)

b = Date(2012, 12, 21)
print(a is b)

del a
print(Date._cache)

del b
print(Date._cache)
