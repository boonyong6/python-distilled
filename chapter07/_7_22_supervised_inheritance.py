import inspect


class Base:
    # Triggered upon the definition of any child class, even if
    #   the child class doesn't directly inherit `Base`.
    @classmethod
    def __init_subclass__(cls):
        curr_frame = inspect.currentframe()
        if curr_frame is None or curr_frame.f_back is None:
            return
        print(f"Initializing {cls} at line {curr_frame.f_back.f_lineno}")


class A(Base):  # <--
    pass


class B(A):  # <--
    pass


# Example: Class registration
class DecoderBase:
    _registry = {}

    @classmethod
    def __init_subclass__(cls):
        attr_name = "mimetypes"
        if not hasattr(cls, attr_name):
            return

        for mt in getattr(cls, attr_name):
            DecoderBase._registry[mt] = cls


# Factory function that uses the registry.
def create_decoder(mimetype):
    return DecoderBase._registry[mimetype]()


class TextDecoder(DecoderBase):
    mimetypes = ["text/plain"]

    def decode(self, data): ...


class HTMLDecoder(DecoderBase):
    mimetypes = ["text/html"]

    def decode(self, data): ...


class ImageDecoder(DecoderBase):
    mimetypes = ["image/png", "image/jpg", "image/gif"]

    def decode(self, data): ...


decoder = create_decoder("image/jpg")
print(decoder)


# Example: Create new code - __repr__()
class PointBase:
    @classmethod
    def __init_subclass__(cls):
        args = list(inspect.signature(cls).parameters)
        arg_vals = ", ".join("{self.%s!r}" % arg for arg in args)

        code = "def __repr__(self):\n"
        code += f"  return f'{cls.__name__}({arg_vals})'\n"
        locs = {}
        exec(code, locs)

        # cls.__repr__ = locs["__repr__"]


class Point(PointBase):
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(5, 6)
print(p)


# Example: In the case of multiple inheritance, use super() to ensure
#   all classes that implement __init_subclass__() get called.
class C:
    @classmethod
    def __init_subclass__(cls):
        print("C.init_subclass")
        super().__init_subclass__()  # <--


class D:
    @classmethod
    def __init_subclass__(cls):
        print("D.init_subclass")
        super().__init_subclass__()  # <--


# Output:
#   C.init_subclass
#   D.init_subclass
class E(C, D):
    pass
