#!/usr/bin/python3
"""Module of basegeometry class"""


class BaseGeometry:
    """ baseGeometry Class """

    def area(self):
        """ Not Yet Implemented """
    
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value name is assumed to be a string"""

        if type(value) != int:
            mesg = "{:s} must be an integer".format(name)
            raise TypeError(mesg)
        if value <= 0:
            mesg = "{:s} must be greater than 0".format(name)
            raise ValueError(mesg)
