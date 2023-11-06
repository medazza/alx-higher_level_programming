#!/usr/bin/python3
"""Module:lookup"""


def lookup(obj):
    """function that returns the list of available
    attributes and methods of an object
    Args:
        obj: object.
    Return:
        list of attributes
    """

    return (dir(obj))
