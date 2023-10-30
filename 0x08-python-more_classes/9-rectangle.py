#!/usr/bin/python3
"""Module 9-rectangle
contains one Rectangle class"""


class Rectangle:
    """Represent a rectangle  class.
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

    def __str__(self):
        """Returns a string repre of  rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.width for i in range(self.height))

    def __repr__(self):
        """Returns a string repre of the rectangle"""
        
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes the rectangle instance obj"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the width of the rectangle if: > 0 and int"""
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter the height of the rectangle"""
        
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the height of the rectangle if: > 0 and int"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns Area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns Perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (self.width + self.height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the Area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with height == width == size"""
        return cls(size, size)
