#!/usr/bin/python3


def add_integer(a, b=98):

    """
    add_integer - Adds and returns two integers

    *** Floats are cast to ints before addition ***

    Args:
        a: The first parameter.
        b: The second parameter.

    Returns:
    The addition of the two given numbers

    Raises:
        - TypeError: if a or b arent integer and if int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
