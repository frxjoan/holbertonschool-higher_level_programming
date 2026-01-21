#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix."""
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(lst, list) for lst in matrix)):
        raise TypeError(err_matrix)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])

    for lst in matrix:
        if len(lst) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for el in lst:
            if not isinstance(el, (int, float)):
                raise TypeError(err_matrix)

    nm = []
    for lst in matrix:
        nl = []
        for el in lst:
            nl.append(round(el / div, 2))
        nm.append(nl)
    return nm
