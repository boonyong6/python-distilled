import encodings

output = "hello"
encoded_output = output.encode("utf-8")  # Encode to bytes.
print(encoded_output)

input_var = b"world"
decoded_input = input_var.decode("utf-8")  # Decode to text.
print(decoded_input)

a = b'Spicy Jalape\xf1o'  # Invalid UTF-8
# a.decode("utf-8")  # Raise UnicodeDecodeError
decoded_a = a.decode("utf-8", "surrogateescape")
print(decoded_a)
encoded_a = decoded_a.encode("utf-8", "surrogateescape")
print(encoded_a)
