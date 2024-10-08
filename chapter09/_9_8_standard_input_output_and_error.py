import sys

# # Example
# sys.stdout.write("Enter your name: ")
# name = sys.stdin.readline()


# Example
name = input("Enter your name: ")
print(f"{name=}")


# Example
with open("input.txt") as file:
    sys.stdin = file
    line = input()
    print(line)

sys.stdin = sys.__stdin__  # Restore the original value.
user_input = input("Enter a value: ")
print(f"{user_input=}")
