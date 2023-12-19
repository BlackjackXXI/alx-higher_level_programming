#!/usr/bin/python3
class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """class begin"""
        if self.__valid_size(size):
            self.__size = size

    @property
    def size(self):
        """Gets size"""
        return self.__size

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    def __valid_size(self, size):
        """Checks if its a positive integer"""
        if isinstance(size, int):
            if size >= 0:
                return True
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size needs to be an integer")
        return False

    @size.setter
    def size(self, value):
        """Sets size."""
        if self.__valid_size(value):
            self.__size = value
