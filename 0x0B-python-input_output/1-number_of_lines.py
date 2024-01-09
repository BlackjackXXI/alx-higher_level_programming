#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) and returns the number of characters writte"""


def number_of_lines(filename=""):
    """Reads file and returns the number of lines

    Args:
    filename (str): String

    Returns:
    none
    """
    with open(filename, encoding="utf-8") as myFile:
        lineCount = 0
        for line in myFile:
            lineCount += 1
        return lineCount
