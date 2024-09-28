# Example: Proxy implementation using __getattr__().
class A:
    def spam(self):
        print("A.spam")

    def grok(self):
        print("A.grok")

    def yow(self):
        print("A.yow")


class LoggedA:
    def __init__(self):
        self._a = A()

    # If an attribute is not defined in this class, delegate it to another object using __getattr__().
    def __getattr__(self, name):
        print("Accessing", name)

        # Delegate to internal A instance.
        return getattr(self._a, name)


a = LoggedA()
a.spam()
a.yow()

print()


# Example: Alternative to inheritance.
class B:
    def __init__(self):
        self._a = A()

    def grok(self):  # <--
        print("B.grok")

    def __getattr__(self, name):
        return getattr(self._a, name)


b = B()
b.spam()  # A.spam
b.grok()  # B.grok (redefined method)
b.yow()  # A.yow


# Example: Does not apply to operations mapped to special methods such as __len__(), __getitem__(), and so on.
class ListLike:
    def __init__(self):
        self._items = list()

    # Can only forward standard methods such as sort(), append(), and so on.
    def __getattr__(self, name):
        return getattr(self._items, name)

    # Explicitly implement the required special methods.
    def __len__(self):
        return len(self._items)


a = ListLike()
a.append(1)  # Works
a.insert(0, 2)  # Works
a.sort()  # Works
len(a)  # Works (explicitly implemented)
# a[0]  # Fails. No __getitem__() method
