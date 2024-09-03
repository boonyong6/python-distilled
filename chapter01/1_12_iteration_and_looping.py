# To loop over a range of integers.
for n in range(1, 10):  # stop = 10 (exclusive)
    print(f"2 to the {n} power is {2**n}")

# Descending sequence
for i in range(8, 1, -1):  # step = -1
    print(i)

# To loop over a dict.
prices = {"GOOG": 490.10, "IBM": 91.50, "AAPL": 123.15}
# Print out all of the members of a dictionary
for key in prices:
    print(key, "=", prices[key])
