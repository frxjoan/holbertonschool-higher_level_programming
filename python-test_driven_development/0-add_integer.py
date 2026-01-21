#!/usr/bin/python3
"""
    Adds two integers.

    a and b must be integers or floats.
    Floats are casted to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after checking their types.

    a and b must be integers or floats.
    Floats are casted to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (a != a or a in (float("inf"), float("-inf"))):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b in (float("inf"), float("-inf"))):
        raise TypeError("b must be an integer")

    try:
        return int(a) + int(b)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")
