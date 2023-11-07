#!/usr/bin/python3
"""Module contains the function "append_write" """


def append_write(filename="", text=""):
    """returns number of chars appended to "filename" from "text" """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
