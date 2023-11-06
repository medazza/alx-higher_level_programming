#!/usr/bin/python3
"""Module contains the class MyInt"""


class MyInt(int):
    """class MyInt that inherits from int:
        MyInt is a rebel.
        MyInt has == and != operators inverted
    """
    def __new__(cls, *args, **kwargs):
        """create a new obj of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now == (equals)"""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now != (deferent)"""
        return int(self) == other
