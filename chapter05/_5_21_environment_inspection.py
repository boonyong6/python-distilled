import inspect
import sys
from collections import ChainMap
from types import FrameType
from typing import cast


def add_then_mul10(x, y):
    z = x + y
    mul10(z)


def mul10(a):
    b = a * 10

    curr_frame = inspect.currentframe()
    if curr_frame is None or curr_frame.f_back is None:
        return

    # Local variables of the current function.
    print("inspect:", curr_frame.f_locals)
    print("sys:", sys._getframe(0).f_locals)

    # Local variables of the caller.
    print("inspect:", curr_frame.f_back.f_locals)
    print("sys:", sys._getframe(1).f_locals)


add_then_mul10(2, 3)


# Instrumenting
def debug(*varnames):
    curr_frame = cast(FrameType, inspect.currentframe())
    caller = cast(FrameType, curr_frame.f_back)
    vars = ChainMap(caller.f_locals, caller.f_globals)
    print(f"{caller.f_code.co_filename}:{caller.f_lineno}")
    for name in varnames:
        print(f"  {name} = {vars[name]!r}")


def func(x, y):
    z = x + y
    debug("x", "y")  # Shows x and y along with file/line
    return z


func(5, 6)


def func1():
    gn = globals()
    gn["func1_var"] = "THE dict (global namespace)"

def func2():
    func1()
    print(func1_var) # type: ignore

func2()