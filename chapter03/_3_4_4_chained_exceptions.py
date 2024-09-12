class ApplicationError(Exception):
    pass


def do_something():
    x = int("N/A")  # Raise ValueError


# Example: Chain exception - Raise an exception while handling another exception.
def spam():
    try:
        do_something()
    except Exception as e:
        raise ApplicationError("It failed") from e  # <--


try:
    spam()
except ApplicationError as e:
    print("It failed. Reason:", e.__cause__)  # <--


# Example: An unexpected exception is raised while handling another exception.
def spam_bugged():
    try:
        do_something()
    except Exception as e:
        print("It failed:", err)  # err undefined (typo)


try:
    spam_bugged()
except Exception as e:
    print("It failed. Reason:", e)
    if e.__context__:
        print("While handling:", e.__context__)  # <--
