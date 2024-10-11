import hashlib

hashing = hashlib.new("sha256")

# Feed data.
hashing.update(b"Hello")
hashing.update(b"World")

print(hashing.digest())
print(hashing.hexdigest())
print(hashing.digest_size)
