#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = sorted(a_dictionary.keys())
    for el in lst:
        print("{}: {}".format(el, a_dictionary[el]))
