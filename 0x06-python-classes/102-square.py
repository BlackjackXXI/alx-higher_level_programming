#!/usr/bin/python3
class Square:
    """returns the current square area"""
    def __init__(self, size=0):
        """class begin"""
        self.size = size

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if self.__valid_size(value):
            self.__size = value

    def __valid_size(self, size):
        """Checks if its a positive integer."""
        if isinstance(size, int) or isinstance(size, float):
            if size >= 0:
                return True
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size needs be a number")
        return False

    def __lt__(self, check):
        """less than"""
        return (self.area() < check.area())

    def __le__(self, check):
        """less than or equal"""
        return (self.area() <= check.area())

    def __eq__(self, check):
        """equal"""
        return (self.area() == check.area())

    def __ne__(self, check):
        """not equal"""
        return (self.area() != check.area())

    def __gt__(self, check):
        """greater than"""
        return (self.area() > check.area())

    def __ge__(self, check):
        """greather than or equal"""
        return (self.area() >= check.area())
