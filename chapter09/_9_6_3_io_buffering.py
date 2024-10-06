data = b"Some data"

# Open a binary-mode file with no I/O buffering.
with open("data.bin", "wb", buffering=0) as file:
    file.write(data)
