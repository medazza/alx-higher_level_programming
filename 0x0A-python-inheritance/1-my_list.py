#!/usr/bin/python3
"""Module: contains 1 Class that inherits from list"""


class MyList(list):
    """ Class inherits from list class"""

    def print_sorted(self):
        """Func prints the list, but sorted in a ascending sort"""
        print(sorted(self))
