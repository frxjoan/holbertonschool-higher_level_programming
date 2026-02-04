#!/usr/bin/python3
'''This function returns a list'''


def inherits_from(obj, a_class):
    '''This function returns a list'''
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
