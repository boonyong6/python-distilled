# readport.py
#
# Reads a file of 'NAME,SHARES,PRICE' data

import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                holding = (name, shares, price)
                portfolio.append(holding)
            except ValueError as err:
                print("Bad row:", row)
                print("Reason:", err)
    return portfolio
