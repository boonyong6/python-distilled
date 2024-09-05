from collections import Counter

# Use case 1: To define an object that consists of named fields.
s = {"name": "GOOG", "shares": 100, "price": 490.10}

# Use case 2: Used as a mapping for performing fast lookups.
prices = {"GOOG": 490.1, "AAPL": 123.5, "IBM": 91.5, "MSFT": 52.13}

# To iterate over the dict.
for sym, price in prices.items():
    print(f'{sym} = {price}')

# To test the presence of a key.
if "IBM" in prices:
    p = prices["IBM"]
else:
    p = 0.0
# A compact equivalent.
p = prices.get("IBM", 0.0)

# To remove an element.
del prices["GOOG"]
print(prices)

# Use tuple to construct composite key.
prices = {}
prices[("IBM", "2015-02-03")] = 91.23
prices["IBM", "2015-02-04"] = 91.42  # Parens omitted

# Convert to dict and calculate total shares.
portfolio = [
    ("ACME", 50, 92.34),
    ("IBM", 75, 102.25),
    ("PHP", 40, 74.50),
    ("IBM", 50, 124.75),
]

total_shares = {s[0]: 0 for s in portfolio}  # dict comprehension
for name, shares, _ in portfolio:
    total_shares[name] += shares

print(total_shares)

# Use the Counter type instead of dict comprehension
total_shares = Counter()  # Dict subclass
for name, shares, _ in portfolio:
    total_shares[name] += shares

print(total_shares)

# Empty dict
prices = {}
prices = dict()

# To create from key-value values.
pairs = [("IBM", 125), ("ACME", 50), ("PHP", 40)]
d = dict(pairs)
print(d)

# To get a list of dictionary keys.
syms = list(d)
print(syms)
syms = d.keys()  # Actively reflects changes
print(syms)
