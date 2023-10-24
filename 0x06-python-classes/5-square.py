#!/usr/bin/python3
"""Square Module."""

class Square:
    """A square class."""

    def __init__(self, size):
        """Constructor a new square.
        Args:
            size (int): The size of square object.
        """
        self.size = size

    @property
    def size(self):
        """Getter the current size of square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Getter the current size of square object."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calc  area of the square object."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #."""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
