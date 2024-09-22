def countup(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1


def countdown(start):
    n = start
    while n > 0:
        yield n
        n -= 1


def up_and_down(n):
    yield from countup(n)
    yield from countdown(n)


# # Without yield from.
# def up_and_down(n):
#     for x in countup(n):
#         yield x
#     for x in countdown(n):
#         yield x

for x in up_and_down(3):
    print(x, end=" ")

print()


# Recursively iterate through nested iterables via recursion.
def flatten(items):
    for i in items:
        if isinstance(i, list):
            yield from flatten(i)  # <--
        else:
            yield i

# Put data on an internal list as opposed to the internal interpreter stack to work around recursion limitations.
def flatten_stack(items):
    stack = [iter(items)]
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()

a = [1, 2, [3, [4, 5], 6, 7], 8]
for x in flatten_stack(a):
    print(x, end=" ")
