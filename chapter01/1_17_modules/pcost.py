# pcost.py

# To import a module under a different name.
import readport as rp

# # To import specific definitions.
# from readport import read_portfolio


def portfolio_cost(filename):
    """
    Compute the total shares*price of a portfolio
    """
    port = rp.read_portfolio(filename)
    return sum(shares * price for _, shares, price in port)
