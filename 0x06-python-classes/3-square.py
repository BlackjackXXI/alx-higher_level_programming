#!/usr/bin/python3
class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """class begin"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size needs to be an integer")

    def area(self):
        """Returns area of the square."""
        return (self.__size ** 2)
