#!/usr/bin/python3
"""
12-pascal_triangle module
"""


def pascal_triangle(n):
    """
    returns list of lists
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(0, n - 1):
        triangle.append([])
        for m in range(len(triangle[i]) + 1):
            a = 0 if m is 0 else triangle[i][m - 1]
            b = 0 if m is (len(triangle[i])) else triangle[i][m]
            triangle[i + 1].append(a + b)
    return triangle
