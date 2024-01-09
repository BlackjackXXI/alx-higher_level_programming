#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""

import json


def from_json_string(my_str):
    """returns the generated object from a "JSON file."

    Args:
    my_str (str): the jason file to append

    Returns:
    object expressed through a jason-formatted string
    """
    return json.loads(my_str)
