def compute_remainder(dividend: int, divisor: int) -> int:
    """
    Computes the remainder.
    """
    quotient = dividend // divisor
    result = dividend - quotient * divisor
    return result


print(compute_remainder(75, 9))


def divide(dividend: int, divisor: int) -> tuple[int, int]:
    """
    Computes the quotient and remainder.
    """
    quotient = dividend // divisor
    remainder = dividend - quotient * divisor
    return (quotient, remainder)


quotient, remainder = divide(1456, 33)


# Parameter default value
def connect(hostname, port, timeout=300):
    print(f"{hostname}:{port}")


# Recommended to specify optional arguments using keyword arguments.
connect("www.python.org", 80, timeout=500)
