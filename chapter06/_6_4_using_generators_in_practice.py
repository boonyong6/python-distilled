# Searches a directory of Python files for all comments containing the word "spam".

import pathlib
import re

for path in pathlib.Path(".").rglob("*.py"):
    if path.exists():
        with path.open("rt", encoding="latin-1") as file:
            for line in file:
                m = re.match(".*(#.*)$", line)
                if m:
                    comment = m.group(1)
                    if "spam" in comment:
                        print(comment)

# Refactored version
def get_paths(top_dir, pattern):
    for path in pathlib.Path(top_dir).rglob(pattern):
        if path.exists():
            yield path

def get_files(paths):
    for path in paths:
        with path.open("rt", encoding="latin-1") as file:
            yield file

def get_lines(files):
    for file in files:
        yield from file  # Produces values (lines) from file object.

def get_comments(lines):
    for line in lines:
        m = re.match(".*(#.*)$", line)
        if m:
            yield m.group(1)

def print_matching(lines, substring):
    for line in lines:
        if substring in line:
            print(substring)

# Generators are hooked together into a workflow.
paths = get_paths(".", "*.py")
files = get_files(paths)
lines = get_lines(files)
comments = get_comments(lines)

print_matching(comments, "spam")
