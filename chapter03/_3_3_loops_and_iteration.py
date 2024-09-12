# An iterable that contains iterables of identical size.
s = [(1, 2, 3), (4, 5, 6)]

# Unpack a tuple into separate iteration variables.
for x, _, z in s:  # _ is a throw-away variable.
    print("x:", x, "z", z)


# An iterable that contains iterables of different sizes.
s = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]

# Use wildcard unpacking (*) to place multiple values into a list variable.
for x, y, *extra in s:
    print("x:", x, "y:", y, "extra:", extra)


# To keep track of a numerical index.
for i, (x, _, *extra) in enumerate(s, start=1):  # To use a different start value.
    print("i:", i, "x:", x, "extra:", extra)


# A common looping problem - iterating in parallel over two or more iterables.
seq1 = [0, 1, 2, 3, 4, 5, 6]
seq2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for seq1_item, seq2_item in zip(seq1, seq2):  # Combine iterables into an iterator of tuples.
    print("seq1_item:", seq1_item, "|", "seq2_item:", seq2_item)


# for-else
# Use case: In code that iterates over data but needs to set or check some kind of flag or condition.
with open("foo.txt") as file:
    for i, line in enumerate(file):
        stripped = line.strip()
        if not stripped:  # If the line is empty.
            break  # Skip the else clause. (Loop is exited early.)
        print(f"=> Line {i + 1}: {stripped}")
    else:  # Execute only if the loop runs to completion.
        raise RuntimeError(
            "No empty lines found."
        )  # Assuming an empty line is expected.
