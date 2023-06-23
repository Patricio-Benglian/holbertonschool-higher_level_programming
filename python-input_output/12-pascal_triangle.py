#!/usr/bin/python3
"""
pascal_triangle module
"""


def pascal_triangle(n):
    """
    returns list of lists representing pascals triangle to nth height
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(0, n - 1):
        triangle.append(
            [
                (0 if m == 0 else triangle[i][m - 1])
                + (0 if m == (len(triangle[i])) else triangle[i][m])
                for m in range(len(triangle[i]) + 1)
            ]
        )
    return triangle
