#!/usr/bin/python3
"""a function that returns integers representing
the Pascal's triangle of a given integer(n)
"""


def pascal_triangle(n):
    """defines a pascal triangle of size `n`"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
