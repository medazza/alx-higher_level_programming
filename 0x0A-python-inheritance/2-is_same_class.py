#!/usr/bin/python3
"""Module contains 1 class (is_same_class)"""


def is_same_class(obj, a_class):
    """ function that returns True if the object is
    exactly an instance of the specified class
    otherwise False
    Args:
        obj and a_class
    Return:
            true or false
    """
    return type(obj) == a_class
