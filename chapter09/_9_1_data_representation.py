a: bytes

# Specify a bytes literal (note the b' prefix).
a = b"hello"

# Specify bytes from a list of integers.
b = bytes([0x68, 0x65, 0x6C, 0x6C, 0x6F])
print(b)

# Create and populate a bytearray from parts.
c = bytearray()
c.extend(b"world")
c.append(0x21)
print(c)  # Print bytearray(b'world!')

# Access byte values.
print(a[0])  # Print 104
print(type(a[0]))  # Print <class 'int'>

for x in b:  # Print 104 101 108 108 111
    print(x, end=" ")
