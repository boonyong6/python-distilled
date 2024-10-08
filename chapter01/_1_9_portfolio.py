# File containing lines of the form "name,shares,price"
filename = 'portfolio.csv'

portfolio = []
with open(filename) as file:
    for line in file:
        row = line.split(',')
        name = row[0]
        shares = int(row[1])
        price = float(row[2])
        holding = (name, shares, price)
        portfolio.append(holding)

print(f'List of tuples: {portfolio}')

total = 0.0
for name, shares, price in portfolio:
    total += shares * price
print(f'total: {total}')

# Or use a list comprehension.
total = sum([shares * price for _, shares, price in portfolio])
print(f'total: {total}')
