#!/usr/bin/python3
"""Module: defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if it possible.
    Args:
        obj (any): Object to add an attribute to.
        att (str): Name of the attribute to add to obj.
        value (any): Value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
