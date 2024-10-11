import os.path

# Example 1:
#   os.path.split(), os.path.join()
filename = "/Users/ben/Desktop/old/data.csv"

splitted_pathname = os.path.split(filename)
print(splitted_pathname)

joined_pathname = os.path.join("/Users/ben/Desktop/", "out.txt")
print(joined_pathname)


# Example 2: 
#   Used in function.
def clean_line(line: str):
    # Line up a line (whatever)
    return line.strip().upper() + "\n"


def clean_data(filename):
    dirname, basename = os.path.split(filename)
    newname = os.path.join(dirname, basename + ".clean")

    with open(newname, "w") as out_f, open(filename, "r") as in_f:
        for line in in_f:
            out_f.write(clean_line(line))


clean_data("filename.txt")


# Example 3:
#   isfile(), isdir(), getsize()
#   Compute the total size in bytes of a file or all files in a directory.
def compute_usage(filename):
    if os.path.isfile(filename):
        return os.path.getsize(filename)
    elif os.path.isdir(filename):
        result = sum(compute_usage(os.path.join(filename, name)) 
                     for name in os.listdir(filename))
        return result
    else:
        raise RuntimeError("Unsupported file kind.")

path = os.path.abspath(".")
print(f'"{path}" takes up {compute_usage(path) / 1024:.1f} KB.')
