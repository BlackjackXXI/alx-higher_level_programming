#!/usr/bin/python3
"""Function to read a text file (UTF8) and print it to stdout"""


def read_file(filename=""):
    """Reads a text file UTF8 and prints it to stdout

    Args:
    filename (str): String

    Returns:
    None
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
