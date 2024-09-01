a = 5
b = 6

if a < b:
    print("Computer says Yes")
else:
    print("Computer says No")

# Use pass to create an empty clause.
if a < b:
    pass  # Do nothing
else:
    print("Computer says No")

# Multiple-test cases
suffix = ".png"

if suffix == ".htm":
    content = "text/html"
elif suffix == ".jpg":
    content = "image/jpeg"
elif suffix == ".png":
    content = "image/png"
else:
    raise RuntimeError(f"Unknown content type {suffix!r}")

print(content)

# Conditional expression
max_val = a if a > b else b
print(max_val)

# Use := to combine the assignment of a variable and a conditional.
print("Assignment expression (walrus operator):")

x = 0
while (x := x + 1) < 10:  # Print 1, 2, 3, ..., 9
    print(x)
