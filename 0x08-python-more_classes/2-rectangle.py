#!/usr/bin/python3
"""
2-rectangle Module
Contains one class Rectangle with private width and height attr,
and area and perimeter methods public
"""


class Rectangle:
    """
    Rectangle class with private attr width and height

    Args:
        width (int): width
        height (int): height

    Methods:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Constractor rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of width if  > 0 and integer """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of height if > 0 and integer """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return  area = width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Return 2*(width + height) (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
