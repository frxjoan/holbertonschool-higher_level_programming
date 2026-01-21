#!/usr/bin/python3
"""
Module print_square.

This module defines a function that prints a square made of '#'
characters based on a given size.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size (width and height) of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
