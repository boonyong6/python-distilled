# Use classes containing a collection of static methods to implement strategy pattern.
class StandardPolicy:
    @staticmethod
    def deposit(account, amount):
        account.balance += amount

    @staticmethod
    def withdraw(account, amount):
        account.balance -= amount

    @staticmethod
    def inquiry(account):
        return account.balance


class EvilPolicy(StandardPolicy):
    @staticmethod
    def deposit(account, amount):
        account.balance += 0.95 * amount

    @staticmethod
    def inquiry(account):
        import random

        if random.randint(0, 4) == 1:
            return 1.10 * account.balance
        else:
            return account.balance


class Account:
    def __init__(self, owner, balance, *, policy=StandardPolicy):
        self.owner = owner
        self.balance = balance
        self.policy = policy

    def __repr__(self):
        return (
            f"Account({self.owner!r}, {self.balance!r}, policy={self.policy.__name__})"
        )

    def deposit(self, amount):
        self.policy.deposit(self, amount)

    def withdraw(self, amount):
        self.policy.withdraw(self, amount)

    def inquiry(self):
        return self.policy.inquiry(self)


a = Account("Guido", 1000.0)
print(a)  # Account('Guido', 1000.0, policy=StandardPolicy)

a.deposit(500)
print(a.inquiry())  # 1500.0

a.policy = EvilPolicy
print(a)  # Account('Guido', 1500.0, policy=EvilPolicy)
a.deposit(500)
print(a.inquiry())  # 1975.0 (Could randomly be 1.10x more)
