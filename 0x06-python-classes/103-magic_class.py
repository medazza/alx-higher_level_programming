#!/usr/bin/python3
"""The MagicClass that match exactly a bytecode."""

import math


class MagicClass:
    """Represent a circle class."""

    def __init__(self, radius=0):
        """Constructor a MagicClass.
        Arg:
            radius (float or int): Radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of MagicClass."""
        return (self.__radius * self.__radius * math.pi)

    def circumference(self):
        """Return The circumference of MagicClass."""
        return (math.pi * self.__radius * 2)
