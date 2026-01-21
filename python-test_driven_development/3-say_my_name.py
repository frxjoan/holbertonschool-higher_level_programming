#!/usr/bin/python3
"""
3-say_my_name module.

This module provides a function that prints a formatted name message.
It validates input types to ensure both first and last names are strings
before displaying the result.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted message displaying the first name and last name
    after validating that both arguments are strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
