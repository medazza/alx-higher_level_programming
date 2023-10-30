#!/usr/bin/python3
"""8-rectangle:module 
defines a Rectangle class"""


class Rectangle:
    """Represent a class: rectangle.
    Attributes:
        number_of_instances (int): Number of Rectangle instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor a new rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter the width of rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter the width of rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter the height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter the height of rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return Area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Return Perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return (0)

        return (self.width + self.height) * 2

    def __str__(self):
        """Returns a string repre of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            if i != self.height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """Returns a string repres of the rectangle to recreate a new instance"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes an instance obj of the rectangle"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns Biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
