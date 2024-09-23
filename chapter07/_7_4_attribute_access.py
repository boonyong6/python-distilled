from account import Account

# Three basic operations:
a = Account("Guido", 1000.0)

print(a.owner)  # 1. get

a.balance = 750.0  # 2. set
print(a.balance)

del a.balance  # 3. delete
try:
    print(a.balance)  # Raise an AttributeError exception.
except AttributeError as e:
    print(e)

# Add new attributes after `a` is created.
a.creation_date = "2019-02-14"  # type: ignore
a.nickname = "Former BDFL"  # type: ignore
print(vars(a))
print()


# Alternative to dot (.) operator - getattr(), setattr(), delattr()
a = Account("Guido", 1000.0)

print(getattr(a, "owner"))

setattr(a, "balance", 570.0)
print(a.balance)

getattr(a, "withdraw")(100)  # Same as a.withdraw(100)
print(vars(a))

print(getattr(a, "balance", "unknown"))
print(getattr(a, "creation_date", "unknown"))

delattr(a, "balance")
print(hasattr(a, "balance"))
print()


# When you access a method as an attribute, you get a bound method.
a = Account("Guido", 1000.0)

w = a.withdraw
print(w)
w(100)
print(a)
