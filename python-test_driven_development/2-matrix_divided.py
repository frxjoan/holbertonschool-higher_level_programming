#!/usr/bin/python3
"""Divides all elements of a matrix by a number and returns a new matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div (rounded to 2 decimals)."""
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            any(len(row) == 0 for row in matrix)):
        raise TypeError(err_matrix)

    row_len = len(matrix[0])

    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for el in row:
            if type(el) not in (int, float):
                raise TypeError(err_matrix)

    return [[round(el / div, 2) for el in row] for row in matrix]
