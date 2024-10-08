# Example 1: Use a generator to decouple output from
#   the exact output stream (file, socket).
def countdown(n):
    while n > 0:
        yield f"T-minus {n}\n"
        n -= 1
    yield "Kaboom!\n"


lines = countdown(5)

# To route the above output to a file.
with open("9_11_out.txt", "at") as f:
    # f.writelines(lines)
    ...


# Example 2: Buffered write.
MAX_BUFFER_SIZE = 20


def buffer_write(generator, output_file):
    chunks = []
    buffered_size = 0

    for chunk in generator:
        chunks.append(chunk)
        buffered_size += len(chunk)
        if buffered_size >= MAX_BUFFER_SIZE:
            output = "".join(chunks)
            output_file.write(output)
            print(f"Write {output!r} to {output_file.name}")
            chunks.clear()
            buffered_size = 0

    output_file.write("".join(chunks))
    print(f"Write {output!r} to {output_file.name}")


# Usage:
count = countdown(5)

with open("9_11_output.txt", "wt") as output_file:
    buffer_write(count, output_file)
