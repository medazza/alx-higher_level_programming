#!/usr/bin/python3
"""Square Module."""


class Square:
    """A square class."""

    def __init__(self, size=0):
        """Constructor of new square object.
        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Getter: size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter: size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Define == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define >= compmarison to a Square."""
        return self.area() >= other.area()
