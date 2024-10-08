import pickle

class SomeObject:
    def __init__(self):
        self.some_attr = "Some value."
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}()"

# Example 1: Python-specific data serialization - Pickle
#   Write an object to a file.
obj = SomeObject()
filename = "9_13_output.bin"
with open(filename, "wb") as file:
    pickle.dump(obj, file)  # <--

#   Restore the object
with open(filename, "rb") as file:
    obj = pickle.load(file)  # <--

print(obj)

#   Turn an object into bytes.
data = pickle.dumps(obj)
#   Turn bytes back into an object.
obj = pickle.loads(data)
