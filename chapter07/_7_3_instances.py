from account import Account

a = Account("Guido", 1000.0)
b = Account("Eva", 10.0)

# To view instance variables (attributes).
print(vars(a))
print(vars(b))

print(type(a))
print(type(a).deposit)
