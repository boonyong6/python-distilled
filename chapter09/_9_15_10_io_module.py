# Example 1: Write to a "fake" file.
# Function that expect a file.
def greeting(file):
    file.write("Hello\n")
    file.write("World\n")

# Call the function with a "fake" file.
import io

file = io.StringIO()
greeting(file)

# Get the resulting output.
output = file.getvalue()
print(output)


# Example 2: Read from a "fake" file.
file = io.StringIO("hello\nworld\n")

while line := file.readline():
    print(line, end="")
