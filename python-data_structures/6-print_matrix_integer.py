#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for el in lst:
            print("{} ".format(el), end="")
        print()
