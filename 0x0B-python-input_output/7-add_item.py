#!/usr/bin/python3
"""a script to t retrieves a dictionary representation of a class Student that defines a student by Public instance attributes"""

import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    jlist = load_from_json_file("add_item.json")
except:
    jlist = []

for arg in sys.argv[1:]:
    jlist.append(arg)

save_to_json_file(jlist, "add_item.json")
