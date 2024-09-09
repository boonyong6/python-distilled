nums = [1, 2, 3, 4]
squares = (num * num for num in nums)
print(squares)

print(next(squares))  # 1
print(next(squares))  # 4

for square in squares:
    print(square)

with open("data.txt") as file:
    # Read lines, strip trailing/leading whitespace.
    lines = (t.strip() for t in file)
    # All comments
    comments = (t for t in lines if len(t) > 0 and t[0] == "#")

    for c in comments:
        print(c)
