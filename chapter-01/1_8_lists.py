names = ["Dave", "Paula", "Thomas", "Lewis"]
# Replace the first two items with ["Dave", "Mark", "Jeff"]
names[0:2] = ["Dave", "Mark", "Jeff"]
print(names)

# To concatenate lists.
a = ["x", "y"] + ["z", "z", "y"]
print(a)

# Convert data to list.
letters = list("Dave")
print(letters)

# Lists can contain mix of objects.
mix_objects = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]
print(mix_objects[3][2])