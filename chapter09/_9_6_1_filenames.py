# Example: Low-level integer file descriptor.
import os

# Integer file descriptor.
fd = os.open("filename.txt", os.O_RDONLY)
print(fd)

file = open(fd, "rt")
print(file)

data = file.read()
print(data)
