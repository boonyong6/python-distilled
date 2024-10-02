from ..primitive import lines, text

__all__ = ["Plot2D"]

class Plot2D:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def clear(self):
        print(f"Called {self.clear.__qualname__}()")

if __name__ == "__main__":
    print("Testing Plot2D")
    p = Plot2D(100, 100)
    ...
