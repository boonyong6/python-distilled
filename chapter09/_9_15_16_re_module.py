import re

text = "Today is 3/27/2018. Tomorrow is 3/28/2018."

# Find all occurrences of a date.
print(re.findall(r"\d+/\d+/\d+", text))

# Replace all occurrences of a date with replacement text.
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
