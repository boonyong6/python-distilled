# Rewrite existing methods.
def loud(cls):
    orig_noise = cls.noise

    def noise(self):
        return orig_noise(self).upper()

    cls.noise = noise
    return cls


def annoying(cls):
    orig_noise = cls.noise

    def noise(self):
        return 3 * orig_noise(self)

    cls.noise = noise
    return cls


@annoying
@loud
class Cyclist:
    def noise(self):
        return "On your left!"

    def pedal(self):
        return "Pedaling"


c = Cyclist()
print(c.noise())


# Create new code - __repr__()
import inspect


def with_repr(cls):
    args = list(inspect.signature(cls).parameters)
    arg_vals = ", ".join("{self.%s!r}" % arg for arg in args)

    code = "def __repr__(self):\n"
    code += f"  return f'{cls.__name__}({arg_vals})'\n"
    locs = {}
    exec(code, locs)

    cls.__repr__ = locs["__repr__"]
    return cls


@with_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(5, 6)
print(p)  # Print Point(5, 6)


# Create new code using `dataclass`
from dataclasses import dataclass


@dataclass
class PointDC:
    x: int
    y: int


p = PointDC(2, 3)
print(p)
