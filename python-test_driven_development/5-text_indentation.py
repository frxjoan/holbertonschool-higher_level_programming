#!/usr/bin/python3
"""
Module text_indentation.

This module defines a function that prints a text with two new lines
after each occurrence of '.', '?' and ':' characters.
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?' or ':' character.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print()
            print()
            i += 1
            while (i < len(text) and text[i] == " "):
                i += 1
            continue
        i += 1
