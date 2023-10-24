#!/usr/bin/python3
"""Square module."""


class Square:
    """Represent a square class ."""

    def __init__(self, size=0):
        """Constructor-Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
