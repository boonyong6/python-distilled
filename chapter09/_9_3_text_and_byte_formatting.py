# Format specifier syntax:
#   [fill[align]][sign][0][width][,][.precision][type]

# Use `format()` to format a single value.
x = 123.456
print(format(x, "0.2f"))    # "123.46"
print(format(x, "10.4f"))   # "  123.4560"
print(format(x, "*<10.2f")) # "****123.46"
print()

# Example:
#   fill        : *
#   align       : <, >, ^ (centered)
#   width       : 10
name = "Elwood"
print(format(name, "<10"))  # "Elwood    "
print(format(name, ">10"))  # "    Elwood"
print(format(name, "^10"))  # "  Elwood  "
print(format(name, "*^10")) # "**Elwood**"
print()

# Example:
#   width       : 16
#   ,           : Use thousand separator
#   precision   : .2
#   type        : f (floating point)
x = 123456.78
print(format(x, "16,.2f"))  # "      123,456.78"
print()

# Example:
#   width       : [0]10
#   type        : d, x, b
x = 42
print(format(x, "10d"))     # "        42"
print(format(x, "10x"))     # "        2a"
print(format(x, "10b"))     # "    101010"
print(format(x, "010b"))    # "0000101010"    
print()

# Example:
#   sign        : +
#   width       : [0]10
#   precision   : .2
#   type        : f, e, %
y = 3.1415926
print(format(y, "10.2f"))   # "      3.14"
print(format(y, "10.2e"))   # "  3.14e+00"
print(format(y, "+10.2f"))  # "     +3.14"
print(format(y, "+010.2f")) # "+000003.14"
print(format(y, "+10.2%"))  # "  +314.16%"
print()

# Example: Complex string formatting (f-strings)
x = 123.456
print(f"Value is {x:0.2f}")         # "Value is 123.46"
print(f"Value is {x:10.4f}")        # "Value is   123.4560"
print(f"Value is {2 * x:*<10.2f}")  # "Value is 246.91****"
print()

# Example: Parts of the format specifier can be supplied by other expressions.
y = 3.1415926
width = 8
precision = 3
print(f"{y:{width}.{precision}f}")  # "   3.142"
print()

# Example: End <expr> by `=` to include the literal text of <expr> in the result.
x = 123.456
print(f"{x=:0.2f}")         # "x=123.46"
print(f"{2 * x=:0.2f}")     # "2 * x=246.91"
print()

# Example: Formatting with `!r` or `!s`
# f"{x!r:<spec>}"  # Calls repr(x).__format__("spec")
# f"{x!s:<spec>}"  # Calls str(x).__format__("spec")

# Example: .format() method of strings (alternative to f-strings)
#   {arg:spec} text is replaced by the value of `format(arg, spec)`.
x = 123.456
print("Value is {:0.2f}".format(x))             # "Value is 123.46
print("Value is {0:10.2f}".format(x))           # "Value is     123.46
print("Value is {val:*<10.2f}".format(val=x))   # "Value is 123.46****
print()
#   If `arg` is omitted, arguments are taken in order.
name = "IBM"
shares = 50
price = 490.1
print("{:>10s} {:10d} {:10.2f}".format(name, shares, price))
#   `arg` can refer to a specific argument number or name.
tag = "p"
text = "hello world"
print("<{0}>{1}</{0}>".format(tag, text))
print("<{tag}>{text}</{tag}>".format(tag=tag, text=text))
#   `arg` can't be an arbitrary expression. But, `format()` can perform 
#     limited attribute lookup, indexing, and nested substitutions.
d = {
    "name": "IBM",
    "shares": 50,
    "price": 490.1
}
print("{0[shares]:d} shares of {0[name]} at {0[price]:0.2f}".format(d))
print()

# Example `bytes` and `bytearray` can be formatted using the % operator.
name = b"ACME"
x = 123.456
print(b'Value is %0.2f' % x)                # b'Value is 123.46'
print(bytearray(b"Value is %0.2f") % x)     # bytearray(b'Value is 123.46')
print(b"%s = %0.2f" % (name, x))            # b'ACME = 123.46
#   Use `-` to adjust alignment.
print(b"%10.2f" % x)    # b'    123.46'
print(b"%-10.2f" % x)   # b'123.46    '
#   When working with bytes, text strings are not supported.
name = "Dave"
# print(b"Hello %s" % name)  # Raise TypeError
print(b"Hello %s" % name.encode("utf-8"))
