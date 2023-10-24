#!/usr/bin/python3
"""Square Module ."""


class Square:
    """A square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor a new square object.
        Args:
            *size (int): The size of the square object.
            *position (int, int): The position of the square object.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter the position of the square."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square object."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
