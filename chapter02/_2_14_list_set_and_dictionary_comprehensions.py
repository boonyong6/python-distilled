nums = [1, 2, 3, 4, 5]

# Also possible to apply a filter.
squares = [n * n for n in nums if n > 2]
print(squares)  # [9, 16, 25]


# List comprehensions examples:
# Some data (a list of dictionaries)
portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "MSFT", "shares": 50, "price": 45.67},
    {"name": "HPE", "shares": 75, "price": 34.51},
    {"name": "CAT", "shares": 60, "price": 67.89},
    {"name": "IBM", "shares": 200, "price": 95.25},
]

# Collect all names ['IBM', 'MSFT', 'HPE', 'CAT', 'IBM']
names = [s["name"] for s in portfolio]
print("names:", names)

# Find all entries with more than 100 shares ["IBM"]
more100 = [s["name"] for s in portfolio if s["shares"] > 100]
print("more100:", more100)

# Find the total, shares*price
cost = sum([s["shares"] * s["price"] for s in portfolio])
print("cost:", cost)

# Collect (name, shares) tuples
name_shares = [(s["name"], s["shares"]) for s in portfolio]
print("name_shares:", name_shares)


# Set comprehension - Distinct values
names = {s["name"] for s in portfolio}
print("names:", names)  # {'CAT', 'IBM', 'HPE', 'MSFT'}


# Dictionary comprehension
# Note: Later entries overwrite earlier ones
prices = {s["name"]: s["price"] for s in portfolio}
print("prices:", prices)


# Comprehension with exception handling
values = ["1", "2", "-4", "n/a", "-3", "5"]


def to_int(x):
    try:
        return int(x)
    except ValueError:
        return None


data1 = [to_int(value) for value in values]
print("data1:", data1)

# Note: Double evaluation of to_int()
data2 = [to_int(x) for x in values if to_int(x) is not None]
print("data2:", data2)

# Use := operator to avoid double evaluation
data3 = [v for x in values if (v := to_int(x)) is not None]
print("data3:", data3)

data4 = [v for x in values if (v := to_int(x)) is not None and v > 0]
print("data4:", data4)
