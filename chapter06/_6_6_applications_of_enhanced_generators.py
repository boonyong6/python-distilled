# Example 1
from contextlib import contextmanager


# Everything prior to the yield executes when the manager enters via the __enter__().
# Everything after the yield executes when the manager exits via the __exit__().
@contextmanager
def manager():
    print("Entering")
    try:
        yield "Some value"  # <--
    except Exception as e:
        print("An error occurred", e)
    finally:
        print("Leaving")


with manager() as val:
    print(val)


# The following illustrates how @contextmanger uses the enhanced generator internally (wrapper).
class Manager:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        # Run to the yield.
        return self.gen.send(None)

    def __exit__(self, ty, val, tb):
        # Propagate an exception (if any).
        try:
            if ty:
                try:
                    self.gen.throw(ty, val, tb)
                except ty:
                    return False
            else:
                self.gen.send(None)
        except StopIteration:
            return True


def gen_func():
    print("Entering")
    try:
        yield "Some value"
    except Exception as e:
        print("An error occurred", e)
    finally:
        print("Leaving")


with Manager(gen_func()) as val:
    print(val)


# Example 2: Long-lived task.
def line_receiver():
    data = bytearray()
    line = None
    line_count = 0
    while True:
        # 1. Pause at "yield line" (a value is returned)
        # 2. Resume at "part = yield" (assign the value from
        #   "<generator>.send(<value>)" to a variable).
        part = yield line
        line_count += part.count(b"\n")
        data.extend(part)
        if line_count > 0:
            index = data.index(b"\n")
            line = bytes(data[: index + 1])
            data = data[index + 1 :]
            line_count -= 1
        else:
            line = None


r = line_receiver()
r.send(None)
print(r.send(b"hello "))
print(r.send(b"world\nit "))
print(r.send(b"works!"))
print(r.send(b"\n"))


# `class` version
# Runs slower - Instance attribute lookup is slower than local variable lookup.
class LineReceiver:
    def __init__(self):
        self.data = bytearray()
        self.line_count = 0

    def send(self, part):
        self.line_count += part.count(b"\n")
        self.data.extend(part)
        if self.line_count > 0:
            index = self.data.index(b"\n")
            line = bytes(self.data[: index + 1])
            self.data = self.data[index + 1 :]
            self.line_count -= 1
            return line
        else:
            return None
