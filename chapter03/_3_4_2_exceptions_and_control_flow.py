import sys

if len(sys.argv) != 2:
    # The error message is printed to sys.stderr and an exit code of 1 is returned.
    raise SystemExit(f"Usage: {sys.argv[0]} <filename>")

filename = sys.argv[1]
print(filename)
