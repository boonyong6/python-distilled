class Account:
    """
    A simple bank account
    """

    # Type hints:
    owner: str
    balance: float

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"{type(self).__name__}({self.owner!r}, {self.balance!r})"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def inquiry(self):
        return self.balance
