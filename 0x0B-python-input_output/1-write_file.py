#!/usr/bin/python3
"""Module contains the function wrtie_file """


def write_file(filename="", text=""):
    """returns number of chars written to filename from text """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
