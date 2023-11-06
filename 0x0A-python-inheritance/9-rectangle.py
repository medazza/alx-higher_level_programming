#!/usr/bin/python3

"""Module contains class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class to define object Rectangle from
    BaseGeometry inheritance """

    def __init__(self, width, height):
        """ Constructor of objects"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method calculate the area"""
        return self.__width * self.__height

    def __str__(self):
        """ Method for print is used """
        (mesg) = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return (mesg)
