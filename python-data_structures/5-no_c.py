#!/usr/bin/python3
def no_c(my_string):
    nstr = ""
    for c in my_string:
        if c != "c" and c != "C":
            nstr += c
    return nstr
