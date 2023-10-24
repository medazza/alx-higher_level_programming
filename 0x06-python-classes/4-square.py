#!/usr/bin/python3
"""Define Square Module."""


class Square:
    """ Square class."""

    def __init__(self, size=0):
        """Constructor a new square.
        Args:
            size (int): The size of square object.
        """
        self.size = size

    @property
    def size(self):
        """Getter the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calc and return area of square object."""
        return (self.__size * self.__size)
