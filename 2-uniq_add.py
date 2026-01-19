#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    lst = []
    for el in my_list:
        if el not in lst:
            res += el
            lst.append(el)
    return res
