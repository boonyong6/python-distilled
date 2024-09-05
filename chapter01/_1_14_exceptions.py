# Handle the exception
portfolio = []
with open("portfolio.csv") as file:
    for line in file:
        row = line.split(",")
        try:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            holding = (name, shares, price)
            portfolio.append(holding)
        except ValueError as err:
            print("Bad row:", row)
            print("Reason:", err)

print(portfolio)

try:
    raise RuntimeError("Emulate an exception")
finally:
    print("=> This code will always run")
