import binascii

# Convert binary data into text-based representations and vice-versa.
# * Example 1: Using `binascii` module.
print(binascii.b2a_hex(b"hello"))
print(binascii.a2b_hex(b"68656c6c6f"))
print(binascii.b2a_base64(b"hello"))
print(binascii.a2b_base64(b"aGVsbG8=\n"))
print()

# * Example 2: Using `bytes` methods.
a = b"hello"
hex_text = a.hex()
print(hex_text)
print(bytes.fromhex(hex_text))
print()

# * Example 3: Using `base64` module.
import base64

print(base64.b64encode(a))