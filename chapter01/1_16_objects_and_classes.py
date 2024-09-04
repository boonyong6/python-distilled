class Stack:
    def __init__(self):  # Initialize the stack
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self):
        return f"<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>"

    def __len__(self):
        return len(self._items)


s = Stack()
s.push("Dave")
s.push(42)
s.push([3, 4, 5])
print(s)

x = s.pop()
y = s.pop()
print(x)
print(y)


# Inherit from Stack.
class NumericStack(Stack):
    # New method
    def swap(self):
        a = self.pop()
        b = self.pop()
        self.push(a)
        self.push(b)

    # To change the behavior of an existing method.
    def push(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError("Expected an int or float")
        super().push(item)  # <-


s = NumericStack()
s.push(6)
try:
    s.push("Dave")  # throw TypeError
except TypeError as err:
    print(repr(err))


# Composition
class Calculator:
    def __init__(self):
        self._stack = Stack()

    def push(self, item):
        self._stack.push(item)

    def pop(self):
        return self._stack.pop()

    def add(self):
        self.push(self.pop() + self.pop())

    def mul(self):
        self.push(self.pop() * self.pop())

    def sub(self):
        right = self.pop()
        self.push(self.pop() - right)

    def div(self):
        right = self.pop()
        self.push(self.pop() / right)


calc = Calculator()
calc.push(2)
calc.push(3)
calc.push(4)
calc.mul()
calc.add()
print(calc.pop())
