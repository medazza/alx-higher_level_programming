#!/usr/bin/python3
"""Define a Square module."""

class Square:
    """Represent a square class that can calc area."""

    def __init__(self, size=0):
        """constructor a square object.
        Args:
            size (int): The size of the new square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square object."""
        return (self.__size * self.__size)
