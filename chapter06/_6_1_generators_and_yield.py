def make_nums(len):
    i = 1
    while i <= len:
        yield i
        i += 1

nums = make_nums(3)
print(next(nums))
print(next(nums))
print(next(nums))
# print(next(nums))  # Raises a StopIteration exception.


# To attach a non-None value to the StopIteration exception
def create_gen():
    yield 37
    return 42

gen = create_gen()
print(next(gen))
try:
    print(next(gen))
except StopIteration as e:
    print("stop_iteration_exception.value:", e.value)


# Cleanup in generators.
def countdown(n):
    print(f"Counting down from {n}")
    try:
        while n > 0:
            yield n
            n -= 1
    finally:  # <--
        print(f"Only make it to {n}")

for n in countdown(10):
    if n == 2:
        break
    print(f"Processing {n}...")
