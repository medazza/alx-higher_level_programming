#!/usr/bin/python3

"""Rectangle module with one class."""


class Rectangle:
    """Represent a Rectangle class.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constr a new Rectangle.
        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter the width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the width of Rectangle if: > 0 and int."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter the height of Rectangle if: > 0 and int."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the height of Rectangle if: > 0 and int."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return Area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return Perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width) + (self.__height) * 2)

    def __str__(self):
        """Return the printable repr of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for jnd in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return String repre of Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
