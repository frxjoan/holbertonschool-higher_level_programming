#!/usr/bin/python3
def inherits_from(obj, a_class):
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
