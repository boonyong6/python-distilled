a = [2, 3, 4, 5]    

# Convention for __repr__() is to return an expression string that can be evaluated to re-create the object using eval().
s = repr(a)         
b = eval(s)  # <-- Turns s back into a list.

# If a expression string can't be re-created, return a string of form <...message...>.
g = (x + 1 for x in a)
print(repr(g))  # <-- "<generator object <genexpr> at 0x000001D92C629A10>"
