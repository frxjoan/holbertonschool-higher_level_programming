#!/usr/bin/python3
'''pascal'''


def pascal_triangle(n):
    '''returns a list of lists of integers representing Pascal's triangle'''
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(n - 1):
        prev = triangle[-1]
        new_line = [1]
        for i in range(1, len(prev)):
            new_line.append(prev[i - 1] + prev[i])
        new_line.append(1)
        triangle.append(new_line)

    return triangle
