import time


def after(seconds, func, *args):
    time.sleep(seconds)
    return func(*args)


def add(x, y):
    return x + y


# 1. It's difficult for the caller to identify the cause of the exception because it could be raised by either the outer function or the callback function.
# after("1", add, 2, 3)  # TypeError: 'str' object cannot be interpreted as an integer
# after(1, add, "2", 3)  # TypeError: can only concatenate str (not "int") to str


# 2. To distinguish between these two cases.
# Option 1: Use chained exceptions.
class CallbackError(Exception):
    pass


def after_ce(seconds, func, *args):
    time.sleep(seconds)
    try:
        return func(*args)
    except Exception as e:
        raise CallbackError("Callback function failed.") from e  # <--


delay = 1
x = "5"
y = 6

try:
    r = after_ce(delay, add, x, y)
except CallbackError as e:
    print("It failed. Reason:", e.__cause__)


# Option 2: Use some kind of result instance.
class Result:
    def __init__(self, value=None, error=None):
        self._value = value
        self._error = error

    def result(self):
        if self._error:
            raise self._error
        return self._value


def after_r(seconds, func, *args):
    time.sleep(seconds)
    try:
        return Result(value=func(*args))    # <--
    except Exception as e:
        return Result(error=e)              # <--

r = after_r(1, add, 2, 3)
print(r.result())

# s = after_r("1", add, 2, 3)

t = after_r(1, add, "2", 3)
print(t.result())
