import string


# Example 1: Use the property feature (getter, setter) to validate attribute value.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner  # This will route through the setter.
        self._balance = balance

    @property  # <-- Getter
    def owner(self):
        return self._owner

    @owner.setter  # <--
    def owner(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected str.")
        if not all(c in string.ascii_uppercase for c in value):
            raise ValueError("Must be uppercase ASCII.")
        if len(value) > 10:
            raise ValueError("Must be 10 characters or less.")
        self._owner = value


a = Account("GUIDO", 1000.0)
a.owner = "EVA"
# a.owner = 42              # Raise TypeError: Expected str.
# a.owner = "Carol"         # Raise ValueError: Must be uppercase ASCII.
# a.owner = "RAMAKRISHNAN"  # Raise ValueError: Must be 10 characters or less.


# Example 2: Property methods - getter, setter, and deleter
class SomeClass:
    def __init__(self, attr):
        self.attr = attr

    @property
    def attr(self):
        print("Getting")
        return self._attr

    @attr.setter
    def attr(self, value):
        print("Setting")
        self._attr = value

    @attr.deleter
    def attr(self):
        print("Deleting")
        del self._attr


s = SomeClass("Some value.")
print(s.attr)
del s.attr


# Example 3: Read-only attributes.
class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * self.width + 2 * self.height


b = Box(4, 5)
print(b.area)
print(b.perimeter)
# b.area = 5  # Raise AttributeError: can't set attribute 'area'
