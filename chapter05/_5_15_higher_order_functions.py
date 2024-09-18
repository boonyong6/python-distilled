import time


def after(seconds, func):
    time.sleep(seconds)
    func()


def main():
    name = "Guido"

    # Closure
    def greeting():
        print("Hello", name)

    print("Loading...")
    after(1, greeting)  # Print "Hello Guido"


main()


# A function that create and return other function.
def make_greeting(name):
    def greeting():
        print("Hello", name)

    return greeting


f = make_greeting("Guido")
g = make_greeting("Ada")

f()
g()


# Binding to variables is not a "snapshot".
def make_greetings(names):
    funcs = []
    for name in names:
        # # Closure points to the `name` variable and the value that it was most recently assigned.
        # funcs.append(lambda: print("Hello", name))
        
        # To capture a copy of a variable.
        funcs.append(lambda name=name: print("Hello", name))

    return funcs


a, b, c = make_greetings(["Guido", "Ada", "Margaret"])
# All print "Hello Margaret"
a()
b()
c()
