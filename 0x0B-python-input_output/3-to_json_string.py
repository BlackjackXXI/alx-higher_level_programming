#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation"""

import json


def to_json_string(my_obj):
    """A function that saves an object to a text file by utilizing a JSON representation

    Args:
    my_obj (obj): object to process

    Returns:
    JSON representation of my_obj
    """
    return json.dumps(my_obj)
