class Account:
    """
    A simple bank account
    """

    # Type hints:
    owner: str
    balance: float

    num_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        Account.num_accounts += 1

    def __repr__(self):
        return f"{type(self).__name__}({self.owner!r}, {self.balance!r})"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def inquiry(self):
        return self.balance
