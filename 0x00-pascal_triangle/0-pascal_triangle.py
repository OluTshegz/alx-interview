#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n
    """
    triangle = []

    if n <= 0:
        return triangle
    for x in range(n):
        row = []

        for y in range(x+1):
            if y == 0 or y == x:
                row.append(1)
            else:
                row.append(triangle[x-1][y-1] + triangle[x-1][y])
        triangle.append(row)

    return triangle
