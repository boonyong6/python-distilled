# Example: To detect an EOF condition.
with open("filename.txt") as file:
    while True:
        line = file.readline()
        if not line:  # EOF
            break
        print(line)

with open("filename.txt") as file:
    # Or using walrus operator (:=).
    while line := file.readline():
        print(line)
