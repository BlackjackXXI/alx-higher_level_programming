#!/usr/bin/python3
"""function that returns an object (Python data structure) represented by a JSON string"""


def append_write(filename="", text=""):
    """Adds a string to the end of a text file and provides the count of characters written

    Args:
    filename (str): string
    text     (str): string

    Returns:
    Number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        return myFile.write(text)
