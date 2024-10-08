x = 5
y = 6
z = 7

# Example: Use `file` argument to redirect the output to a file.
with open("out.txt", "at") as f:
    print("The values are", x, y, z, file=f)  # <--


# Example: Use `sep` argument to change the separator character.
print("The values are", x, y, z, sep=",")
