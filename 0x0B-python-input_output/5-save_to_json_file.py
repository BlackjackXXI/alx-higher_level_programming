#!/usr/bin/python3
"""script that adds all arguments to a Python list, and then save them to a file"""

import json


def save_to_json_file(my_obj, filename):
    """returns the generated object from a "JSON file"

    Args:
    my_obj   (obj): object to process
    filename (str): String

    Returns:
    none
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
