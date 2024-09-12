# Example 1:
class Manager:
    def __init__(self, x):
        self.x = x

    def yow(self):
        print("yow")

    def __enter__(self):
        print("Enter a new context.")
        return self

    def __exit__(self, ty, val, tb):
        print("Exit a context.")
        if ty:
            print("💀 Error encountered and 👍 handled.\n")
            return True  # Indicate that the raised exception was handled.


with Manager(6) as m:
    m.yow()
    raise ValueError("Bad input")


# Example 2:
class ListTransaction:
    def __init__(self, the_list):
        self.the_list = the_list

    def __enter__(self):
        self.working_copy = list(self.the_list)
        return self.working_copy

    def __exit__(self, type, value, tb):
        if type is None:
            # Changes only take effect if no exceptions occur.
            self.the_list[:] = self.working_copy  # <--
        return False


items = [1, 2, 3]

with ListTransaction(items) as working:
    working.append(4)
    working.append(5)

print(items)  # -> [1, 2, 3, 4, 5]

try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("We're hosed!")
except RuntimeError:
    pass

print(items)  # -> [1, 2, 3, 4, 5]
