#!/usr/bin/python3
"""Define Base Class"""

import json
import csv
import turtle


class Base:
    """Base Class."""
    __nb_objects = 0

    @staticmethod
    def test_reset():
        """Reset __nb_objects for testing purposes."""
        Base.__nb_objects = 0

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        build_list = []
        try:
            with open(cls.__name__ + ".json", 'r') as my_file:
                read = Base.from_json_string(my_file.read())
                for elm in read:
                    build_list.append(cls.create(**elm))
                return build_list
        except:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        write_list = []
        if list_objs is not None:
            for elm in list_objs:
                write_list.append(cls.to_dictionary(elm))
        with open(cls.__name__ + ".json", 'w') as my_file:
            my_file.write(cls.to_json_string(write_list))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize to csv."""
        with open(cls.__name__ + ".csv", 'w', newline='') as my_file:
            if list_objs is None or len(list_objs) == 0:
                my_file.write("[]")
            elif cls.__name__ is "Rectangle":
                for elm in list_objs:
                    csv.writer(my_file).writerow([elm.id,
                                                  elm.width,
                                                  elm.height,
                                                  elm.x,
                                                  elm.y])
            else:
                for elm in list_objs:
                    csv.writer(my_file).writerow([elm.id,
                                                  elm.size,
                                                  elm.x,
                                                  elm.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize csv."""
        build_list = []
        try:
            with open(cls.__name__ + ".csv", 'r') as my_file:
                for elm in csv.reader(my_file):
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(elm[0]),
                                      "width": int(elm[1]),
                                      "height": int(elm[2]),
                                      "x": int(elm[3]),
                                      "y": int(elm[4])}
                    else:
                        dictionary = {"id": int(elm[0]),
                                      "size": int(elm[1]),
                                      "x": int(elm[2]),
                                      "y": int(elm[3])}
                    build_list.append(cls.create(**dictionary))
        except:
            pass
        return build_list

    def __init__(self, id_=None):
        """Initialize the class."""
        if id_ is not None:
            self.id = id_
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
