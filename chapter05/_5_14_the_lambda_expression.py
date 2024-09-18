a = lambda x, y: x + y
r = a(2, 3)


# To define a callback function.
words = ["apple", "boy", "cat", "dog", "elephant"]
result = sorted(words, key=lambda word: len(set(word)))
print(result)


# Late binding - x is bound at the time of lambda evaluation, not definition.
x = 2
f = lambda y: x * y
x = 3
g = lambda y: x * y
print(f(10))  # 30
print(g(10))  # 30


# To capture variable values at the time of definition.
# This works because default arguments are only evaluated at the time of definition.
x = 2
f = lambda y, x=x: x * y
x = 3
g = lambda y, x=x: x * y
print(f(10))  # 20
print(g(10))  # 30
