items = {"number": 42, "text": "Hello World"}

items["func"] = abs  # Add the abs() function.
import math

items["mod"] = math  # Add a module.
items["error"] = ValueError  # Add an exception type.
nums = [1, 2, 3, 4]
items["append"] = nums.append  # Add a method of another object.

print('items["func"](-45):', items["func"](-45))
print('items["mod"].sqrt(4):', items["mod"].sqrt(4))

try:
    x = int("a lot")
except items["error"] as e:
    print('Handle items["error"] exception: Couldn\'t convert')

items["append"](100)
print("nums:", nums)


# List of types is also a first-class object.
line = "ACME, 100, 490.10"
column_types = [str, int, float]
parts = line.split(",")
row = [ty(val) for ty, val in zip(column_types, parts)]
print("row:", row)
