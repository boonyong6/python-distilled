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
