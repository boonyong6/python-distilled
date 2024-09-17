from typing import NamedTuple


class ParseResult(NamedTuple):
    name: str
    value: str


def parse_value(text: str):
    """
    Split text of the form name=value into (name, val)
    """
    parts = text.split("=", 1)
    return ParseResult(parts[0].strip(), parts[1].strip())


result = parse_value("url=https://www.python.org")
print(result.name, result.value)
