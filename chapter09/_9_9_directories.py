# Example: To get a directory listing.
import os

names = os.listdir("..")
for name in names:
    print(name)

print()


# Example: Matching filenames according to a pattern, known as globbing.
import pathlib

for filename in pathlib.Path(".").glob("*.txt"):
    print(filename)

print()

# Use `rglob()` to recursively search all subdirectories for filenames that 
#   match the pattern.
for filename in pathlib.Path("..").rglob("*.txt"):
    print(filename)
