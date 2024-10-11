import subprocess

# Example 1:
#   Run a command and collect its output.
try:
    out = subprocess.check_output(["ls", "-l"])
    # print(out.decode("utf-8"))
except subprocess.CalledProcessError as e:
    print("It failed:", e)


# Example 2:
# wc is a program that returns line, word, and byte counts.
p = subprocess.Popen(["wc"], 
                     stdin=subprocess.PIPE, 
                     stdout=subprocess.PIPE)

if p.stdin is None or p.stdout is None:
    raise SystemExit("`p.stdin` or `p.stdout` is `None`.")

# Send data to the subprocess.
p.stdin.write(b"hello world\nthis is a test\n")
p.stdin.close()

# Read data back.
out = p.stdout.read()
print(out)
