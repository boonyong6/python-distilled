# Example: Any Python statement is allowed in the body of a class.
debug = True

class Account:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance
    
    if debug:
        import logging
        
        log = logging.getLogger(f"{__module__}.{__qualname__}")

        def deposit(self, amount):
            Account.log.debug("Depositing %f", amount)
            self.balance += amount

        def withdraw(self, amount):
            Account.log.debug("Withdrawing %f", amount)
            self.balance -= amount
    else:
        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            self.balance -= amount
