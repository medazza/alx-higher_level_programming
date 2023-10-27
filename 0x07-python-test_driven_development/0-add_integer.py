#!/usr/bin/python3
"""Module for adding Two integer method."""


def add_integer(a, b=98):
    """Func adds two integers.

    Args:
        a: First integer.
        b: Second integer, by default=98.

    Raises:
        TypeError: if a, b are not int or float.

    Returns:
        Sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
