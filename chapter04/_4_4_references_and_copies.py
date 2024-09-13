a = [1, 2, [3, 4]]


# Shallow copy
b = list(a)  # <--
print("b is a:", b is a)


# Deep copy
import copy
b = copy.deepcopy(a)  # <--
b[2][0] = -100
print("b:", b)
print("a:", a)
