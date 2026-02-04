#!/usr/bin/python3
'''This function returns a list'''


def inherits_from(obj, a_class):
    '''This function returns a list'''
    return isinstance(obj, a_class) and type(obj) is not a_class
