#!/usr/bin/python3

def matrix_divided(matrix, div):

    """
    matrix_divided - divide the mqtrix element

    Args:
        matrix: The matrix to perform upon
        div: The value to divide the matrix elements by

    Returns:
        A new matrix yith results of division

    Raises:
        TypeError: element of the matrix is not an int or float
        TypeError: the matrix rows are not of uniform size
        TypeError: div is not a number
        ZeroDivisionError: div == 0
    """
    flag = 0
    if matrix == []:
        flag = 1
    if any(not isinstance(row, list) for row in matrix):
        flag = 1
    for row in matrix:
        if any(not isinstance(elm, (int, float)) for elm in row):
            flag = 1
    if flag:
        raise TypeError("matrix must be a matrix (list of lists)" + " of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
