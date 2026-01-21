#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for i in range(len(lst)):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(lst[i]), end="")
        print()
