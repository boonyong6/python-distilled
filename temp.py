from typing import Any


class MyClass:
    def __init__(self, attr) -> None:
        self.attr = attr

    def __setattr__(self, name: str, value: Any) -> None:
        print("Calling __setattr__()...", name)
        super().__setattr__(name, value)

    @property
    def attr(self):
        print("Calling attr getter...")
        return self._attr

    @attr.setter
    def attr(self, value):
        print("Calling attr setter...")
        self._attr = value


obj = MyClass(6)
print(obj.__dict__)
print(MyClass.__dict__)
