import time

# n = 2
# print(f"Sleeping for {n} seconds...")
# time.sleep(n)

print(time.time())
print(time.localtime())
print(time.gmtime())  # UTC

print(time.ctime())  # string representation in local time.
print(time.asctime())  # same operation as ctime(), but accept different argument type.
