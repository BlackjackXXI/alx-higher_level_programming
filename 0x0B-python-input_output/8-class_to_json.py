#!/usr/bin/python3
"""script to retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure

    Args:
    obj (obj): object

    Returns:
    dictionary description 
    """
    return obj.__dict__
