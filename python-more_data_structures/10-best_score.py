#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    bestkey = next(iter(a_dictionary))
    bestvalue = a_dictionary[bestkey]
    for key in a_dictionary:
        if a_dictionary[key] > bestvalue:
            bestvalue = a_dictionary[key]
            bestkey = key
    return bestkey
