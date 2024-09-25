from _7_19_multiple_inheritance_interfaces_and_mixins import Duck, Trombonist, Cyclist

handlers = {}


def handler(type):
    def decorator(func):
        handlers[type] = func
        return func

    return decorator


@handler(Duck)
def handle_duck(duck):
    print(f"Invoked {handle_duck.__name__}({duck})")


@handler(Trombonist)
def handle_trombonist(trombonist):
    print(f"Invoked {handle_trombonist.__name__}({trombonist})")


@handler(Cyclist)
def handle_cyclist(cyclist):
    print(f"Invoked {handle_cyclist.__name__}({cyclist})")


# Dispatch that supports inheritance.
def dispatch(obj):
    for ty in type(obj).__mro__:  # <--
        func = handlers.get(ty)
        if func:
            return func(obj)
    raise RuntimeError(f"No handler for {obj}")


class SubclassCyclist(Cyclist):
    pass


obj = SubclassCyclist()
dispatch(obj)


# Class-based dispatch using getattr().
class Dispatcher:
    def handle(self, obj):
        for ty in type(obj).__mro__:
            method = getattr(self, f"handle_{ty.__name__}", None)
            if method:
                return method(obj)

        raise RuntimeError(f"No handler for {obj}")

    def handle_Duck(self, obj):
        print(f"Invoked {self.handle_Duck.__name__}({obj})")

    def handle_Trombonist(self, obj):
        print(f"Invoked {self.handle_Trombonist.__name__}({obj})")

    def handle_Cyclist(self, obj):
        print(f"Invoked {self.handle_Cyclist.__name__}({obj})")


dispatcher = Dispatcher()
dispatcher.handle(Duck())
dispatcher.handle(Cyclist())
