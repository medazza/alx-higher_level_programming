#!/usr/bin/python3

""" Module contains a class that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class to define object Rectangle from
    BaseGeometry inheritance """

    def __init__(self, width, height):
        """ Constructor of class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
