#!/usr/bin/python3
""" function that returns the JSON representation of an object (string)"""


def write_file(filename="", text=""):
    """Writes a string that returns number of characters writte

    Args:
    filename (str): String
    text (str): String

    Returns:
    number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        return myFile.write(text)
