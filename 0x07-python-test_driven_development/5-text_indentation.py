#!/usr/bin/python3
"""Module for text_indentation method(func)."""


def text_indentation(text):
    """Method for adding two new lines after the '.?:' chars.

    Args:
        text: The string text.

    Raises:
        TypeError: If text is not a str(string).
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimtr in ".?:":
        # print(delim, text.split(delim))
        text = (delimtr + "\n\n").join(
            [lne.strip(" ") for lne in text.split(delimtr)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
