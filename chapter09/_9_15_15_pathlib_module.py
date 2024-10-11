from pathlib import Path

# Example 1: Basic usage.
filename = Path("/Users/ben/old/data.csv")

print(filename.name)                        # data.csv
print(filename.parent)                      # \Users\ben\old
print(filename.parent / "new-file.csv")     # \Users\ben\old\new-file.csv
print(filename.parts)                       # ('\\', 'Users', 'ben', 'old', 'data.csv')
print(filename.with_suffix(".csv.clean"))   # \Users\ben\old\data.csv.clean

# Example 2:
#   Re-implementation of the compute_usage() from the previous section.
def compute_usage(filename):
    path = Path(filename)
    if path.is_file():
        return path.stat().st_size
    elif path.is_dir():
        result = sum(path.stat().st_size
                     for path in path.rglob("*")
                     if path.is_file())
        return result
    else:
        raise RuntimeError("Unsupported file kind.")

path = Path(".")
print(f'"{path.absolute()}" takes up {compute_usage(path) / 1024:.1f} KB.')
