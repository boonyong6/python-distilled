from numpy import matrix

m = matrix(
    [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    ]
)

a = m[0:3:2]
print("a:", a)

b = m[1:3, 5:9]
print("b:", b)

c = m[0:3:2, 5:9:3]
print("c:", c)

m[1:4, 6:7] = 666
print("m:", m)

# Use ... to denote trailing or leading dimensions
m[1:3, ...] = 888
print("m:", m)

# The value passed to methods is a tuple.
a = m[..., 5:7]  # a = m.__getitem__((Ellipsis, slice(5, 7, None)))
print("a:", a)
