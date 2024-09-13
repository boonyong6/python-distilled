a = 37
b = a
c = []
c.append(b)

import sys

print(sys.getrefcount(a))


# Example: Circular dependency
a = {}
b = {}
a["b"] = b  # a contains reference to b
b["a"] = a  # b contains reference to a
del a
del b
