def fn(id):
    n = 666

    def nested_fn():
        print(id, n)

    return nested_fn


nested_fn = fn("demon")

print(nested_fn.__qualname__)

closure_vars = nested_fn.__closure__
if type(closure_vars) is tuple:
    print(closure_vars[0].cell_contents)

fn.secure = 1
fn.private = 1


import inspect


def func(x: int, y: float, debug=False) -> float:
    return 0.6

sig = inspect.signature(func)
print(sig)

for param in sig.parameters.values():
    print("name:", param.name)
    print("annotation:", param.annotation)
    print("kind:", param.kind)
    print("default:", param.default)
    print()
