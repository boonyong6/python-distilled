from functools import partial

def func(a, b, c, d):
    print(a, b, c, d)

# To make nonconforming functions match expected calling signatures.
f = partial(func, 1, 2)
f(3, 4)
f(10, 20)

g = partial(func, 1, 2, d=4)
g(3)
g(10)
