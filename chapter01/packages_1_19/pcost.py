# pcost.py

# To relative import a module within the same package.
from . import readport as rp


def portfolio_cost(filename):
    """
    Compute the total shares*price of a portfolio
    """
    port = rp.read_portfolio(filename)
    return sum(shares * price for _, shares, price in port)
