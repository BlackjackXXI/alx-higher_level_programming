#!/usr/bin/python3
"""function that returns the dictionary description with simple data structure for JSON serialization of an object"""

import json


def load_from_json_file(filename):
    """returns the generated object from a "JSON file"

    Args:
    filename (str): String

    Returns:
    the object created
    """
    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
