#!/usr/bin/python3


def add_integer(a, b=98):

    """
    add_integer - function that adds two numbers

    *** Floats adds two integer and/or float numbers ***

    Args:
        a: first number
        b: second number

    Returns:
    addition of the two numbers

    Raises:
        - TypeError: if a or b arent integer and if int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)