def product(first, *args):
    result = first
    for x in args:
        result *= x
    return result

print(product(10, 20))
print(product(2, 3, 4, 5))
