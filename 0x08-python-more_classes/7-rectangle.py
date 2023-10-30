#!/usr/bin/python3
"""Module: 7-rectangle.py
contains one class
"""


class Rectangle:
    """Represent a rectangle class .
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constr a new instance of Rectangle class
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter the width of Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the width of Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter the height of Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the height of Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        return the Area of a rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return the Perimeter of a rectangle instance
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns a string repres of the Rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Returns a string repres of the Rectangle instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of rectangle class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
