a = "Hello World"
b = "Python is groovy"
c = """Computer says no."""
d = """Computer still says no."""

print(a)
print(b)
print(c)
print(d)

print(
    """Content-type: text/html

<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.      
"""
)

# Immediately adjacent string literals are concatenated into a single string.
print(
    "Content-type: text/html\n"
    "\n"
    "<h1> Hello World </h1>\n"
    'Click <a href="http://www.python.org">here</a>.\n'
)

# Alternative to f-strings.
year = 2024
principal = 6789.9876

print("{0:>3d} {1:0.2f}".format(year, principal))
print("%3d %0.2f" % (year, principal))
print()

a = "Hello World"
print(len(a))  # 11
print(a[4])  # 'o'
print(a[-1])  # 'd'

print(a[:5])  # 'Hello'
print(a[6:])  # 'World'
print(a[3:8])  # 'lo Wo'
print(a[-5:])  # 'World'

# Convert string to int/float
x = "37"
y = "42.79"

print(int(x) + float(y))  # 79.78999999999999 (float arithmetic issue)

s = "hello\nworld"
# Print:
#   hello
#   world
print(str(s))
# Print:
#   'hello\nworld'
print(repr(s))

print(format(12.34567, "0.2f"))
print(f"{12.34567:0.2f}")
