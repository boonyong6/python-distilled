from functools import wraps


# Example 1: Decorator with no arguments.
def trace(func):
    @wraps(func)  # Copy function metadata to the replacement function, call().
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@trace
def square(x):
    return x * x


print(square(6))
print(square.__name__)


# Example 2: Decorator with arguments.
def trace_with_arg(message):  # Decorator factory
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message.format(func=func))
            return func(*args, **kwargs)

        return wrapper

    return decorate


# To reuse the decorator instance.
logged = trace_with_arg("You called {func.__name__}")


@logged
def func1():
    pass


@logged
def func2():
    pass


func1()
func2()


# Example 3: Decorator that doesn't replace the original function.
# Event handler decorator
_event_handlers = {}

def event_handler(event):
    def register_function(func):
        _event_handlers[event] = func
        return func
    return register_function

@event_handler("BUTTON")
def handle_button(msg):
    pass

@event_handler("RESET")
def handle_reset(msg):
    pass

print(_event_handlers)
