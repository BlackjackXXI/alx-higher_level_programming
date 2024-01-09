#!/usr/bin/python3
""" function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""


def read_lines(filename="", nb_lines=0):
    """Read X number of lines and prints it to stdout

    Args:
    filename (str): Strin
    nb_lines (int): Integer

    Returns:
    none
    """
    with open(filename, encoding="utf-8") as myFile:
        lineCount = 0
        for line in myFile:
            if lineCount < nb_lines or nb_lines <= 0:
                print(line, end="")
            lineCount += 1
