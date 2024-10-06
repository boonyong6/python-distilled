# Read a text file all at once as string.
with open("filename.txt", "rt") as file:
    data = file.read()
    print(data)

# Read a file line-by-line.
with open("filename.txt", "rt") as file:
    for line in file:
        print(line, end="")

# Write to a text file.
with open("out.txt", "wt") as file:
    file.write("Some output\n")
    print("More output", file=file)  # Write via print().

import os

print(os.getcwd())