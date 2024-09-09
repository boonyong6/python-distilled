# s * n creates shallow copies (reference) of the list.
a = [3, 4, 5]
b = [a]  # Nested list
c = b * 4
print(c)  # [[3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]]
a[0] = -7
print(c)  # [[-7, 4, 5], [-7, 4, 5], [-7, 4, 5], [-7, 4, 5]]

a = [3, 4, 5]
c = [list(a) for _ in range(4)]  # list() makes a copy of "a" (not a reference)
a[0] = -7
print(c)  # [[3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]]

a_last = a[-1]
print('Last of "a":', a_last)

# Named slice
last_two = slice(1, 3)
print("Last two elements:", a[last_two])

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s[0:3] = [6]
print(s)
