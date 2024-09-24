# Non-overridable private attributes (__<attr>)
class A:
    def __init__(self):
        self.__x = 3

    def __spam(self):
        print(f"{A.__spam.__qualname__}", self.__x)
    
    def bar(self):
        self.__spam()

class B(A):
    def __init__(self):
        super().__init__()
        self.__x = 37
    
    def __spam(self):
        print(f"{B.__spam.__qualname__}", self.__x)
    
    def grok(self):
        self.__spam()

b = B()
b.bar()     # A.__spam 3
b.grok()    # B.__spam 37
print(vars(b))  # {'_A__x': 3, '_B__x': 37}
