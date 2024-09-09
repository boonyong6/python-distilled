a = {"x": 1, "y": 2, "z": 3}
b = {"z": 3, "w": 4, "q": 5}
# Set operations also work on the key-view and item-view objects of dictionaries
c = a.keys() & b.keys()
print(c)  # {"z"}
