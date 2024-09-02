#!/usr/bin/env python
# pcost.py
#
# Reads input lines of the form 'NAME,SHARES,PRICE'.
# For example:
#
#   SYM,123,456.78
import sys

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} <filename>")

rows = []
with open(sys.argv[1], "rt") as file:
    for line in file:
        rows.append(line.split(","))

# rows is a list of this form
# [
#   ['SYM', '123', '456.78']
#   ...
# ]

total = sum([int(row[1]) * float(row[2]) for row in rows])
print(f'Total cost: {total:0.2f}')
