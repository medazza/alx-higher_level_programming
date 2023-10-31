#!/usr/bin/python3
"""101-locked_class.py :Module
   contains one locked class."""


class LockedClass:
    """
    class LockedClass with no class or object attribute, 
    that prevents the user from dynamically creating new 
    instance attributes, except if the new instance 
    attribute is called first_name
    """

    __slots__ = ["first_name"]
