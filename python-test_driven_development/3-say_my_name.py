#!/usr/bin/python3
"""Prints a formatted sentence with a person's first and last name."""


def say_my_name(first_name, last_name=""):
    """
    Prints a sentence with the first name and last name.

    first_name and last_name must be strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if last_name is not None and not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
