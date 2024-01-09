#!/usr/bin/python3
"""function that defines a student by: (based on 10-student.py)"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """

        Args:
        first_name (str): first name string
        last_name  (str): last name string
        age (int): age string

        Returns:
        none
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return dictionary representation of Students instance

        Args:
        None

        Returns:
        dictionary representation of a Students instance
        """
        return self.__dict__
