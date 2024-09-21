glob = 6


def func():
    loc = 7
    exec("glob = 666", globals())
    print(glob)

    locs = locals()
    exec("l = 777", None, locs)
    print(loc)
    print(locs["l"])


func()


# Common use: Creating functions and methods.
def make_init(*names):
    params = ",".join(names)
    code = f"def __init__(self, {params}):\n"
    for name in names:
        code += f"  self.{name} = {name}\n"
    d = {}
    exec(code, d)
    return d["__init__"]


class Vector:
    __init__ = make_init("x", "y", "z")


v = Vector(5, 6, 7)  # type: ignore
print(v.y)  # type: ignore
