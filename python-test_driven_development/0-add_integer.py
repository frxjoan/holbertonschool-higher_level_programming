#!/usr/bin/python3
"""
    Adds two integers.

    a and b must be integers or floats.
    Floats are casted to integers before addition.
"""


def add_integer(a, b=98):
    result = 0
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
