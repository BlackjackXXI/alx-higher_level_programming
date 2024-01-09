#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:"""


def pascal_triangle(n):
    """generates a pascal list

    Args:
    n (int): Size of the triangle

    Returns:
    list generated
    """
    lastrow = []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i // 2 + 1):
            row[j] = lastrow[j - 1] + lastrow[j]
            row[i - j] = lastrow[j - 1] + lastrow[j]
        triangle.append(row)
        lastrow = row
    return triangle
