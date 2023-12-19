#!/usr/bin/python3
class Square:
    """class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """class begin"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @property
    def position(self):
        """Gets position"""
        return self.__position

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
            return
        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)

    def __valid_size(self, size):
        """Checks if its a positive integer."""
        if isinstance(size, int):
            if size >= 0:
                return True
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size needs be an integer")
        return False

    def __valid_position(self, position):
        """Checks for a tuple of 2 positive integers."""
        if isinstance(position, tuple):
            if len(position) == 2:
                if isinstance(position[0], int):
                    if isinstance(position[1], int):
                        if position[0] >= 0 <= position[1]:
                            return True
        raise TypeError("position needs to be a tuple of 2 positive integers")
        return False

    @size.setter
    def size(self, value):
        """Sets size"""
        if self.__valid_size(value):
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets position"""
        if self.__valid_position(value):
            self.__position = value
