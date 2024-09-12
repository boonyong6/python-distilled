import traceback


class ApplicationError(Exception):
    pass


def do_something():
    x = int("N/A")  # Raise ValueError


def spam():
    try:
        do_something()
    except Exception as e:
        raise ApplicationError("Failed to convert to int.") from e  # <--


try:
    spam()
except Exception as e:
    # A list of traceback messages.
    tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
    tb_msg = "".join(tb_lines)
    print("It failed:")
    print(tb_msg)
