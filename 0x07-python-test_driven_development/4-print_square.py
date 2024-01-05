#!/usr/bin/python3


def print_square(size):

    """
    print_square - prints a square

    Args:
        size: size of the square base

    Returns:
        None

    Raises:
        TypeError: size is not an integer
        ValueError: size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(('#' * size + '\n') * size, end='')
