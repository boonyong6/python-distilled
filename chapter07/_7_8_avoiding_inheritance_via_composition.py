# Bad use of inheritance. Unrelated methods are also inherited.
class StackInh(list):
    def push(self, item):
        self.append(item)

# In this case, using composition is more appropriate.
class StackComp:
    def __init__(self):
        self._items = list()  # <--
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        self._items.pop()

    def __len__(self):
        return len(self._items)

# Improved version - Composition with dependency injection.
class StackCompDI:
    def __init__(self, *, container=None):  # <--
        if container is None:
            container = list()
        self._items = container

    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        self._items.pop()

    def __len__(self):
        return len(self._items)
    
from array import array

s = StackCompDI(container=array("i"))
s.push(42)
s.push(23)

# Using composition, the implementation detail is hidden, making it easy to change. E.g. change it to use linked tuples.
class StackLT:
    def __init__(self):
        self._items = None
        self._size = 0
    
    def push(self, item):
        self._items = (item, self._items)  # <--
        self._size += 1
    
    def pop(self):
        if self._items is None:
            return None
        
        (item, self._items) = self._items  # <--
        self._size -= 1
        return item
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        return repr(self._items)

s = StackLT()
s.push(5)
s.push(6)
print(s)
print(s.pop())
