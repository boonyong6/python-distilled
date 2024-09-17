# UnboundLocalError example
def func(x):
    if x > 0:
        y = 42
    return x + y  # y not assigned if conditional is false.


print(func(10))  # Returns 52
try:
    print(func(-10))  # UnboundLocalError: y referenced before assignment.
except NameError as e:
    print(repr(e))


# Modify a global variable using `global`.
x = 42
y = 37


def modify_global_var():
    global x  # <--
    x = 13
    y = 0


modify_global_var()
print(f"x is now {x}. y is still {y}.")


# Nested function
def countdown(start):
    n = start

    def display():  # <--
        print("T-minus", n)

    while n > 0:
        display()
        n -= 1


countdown(3)
