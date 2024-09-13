# Compare two objects
def compare(a, b):
    if a is b:
        print("Same object")
    if a == b:
        print("Same value")
    if type(a) is type(b):
        print("Same type")


a = [1, 2, 3]
b = [1, 2, 3]

print("=> compare(a, a)")
compare(a, a)
print()

print("=> compare(a, b)")
compare(a, b)
print()

print("=> compare(a, [4, 5, 6])")
compare(a, [4, 5, 6])
print()


# Preferred way to check a value against a type.
if isinstance(a, (list, tuple)):  # Can check against many types.
    max_val = max(a)
