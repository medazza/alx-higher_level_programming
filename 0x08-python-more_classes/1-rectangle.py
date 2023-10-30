#!/usr/bin/python3
"""
2-rectangle module
Contains one class named Rectangle
with private attribute: width and height
"""


class Rectangle:
    """
    The Rectangle class with private attribute width and height
    Args:
        width (int): width
        height (int): height
    Methods:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initialisation of rectangle instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of width if > 0 and integer """
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
        """ Setter of height if  > 0 and integer """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
