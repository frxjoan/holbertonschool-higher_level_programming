#!/usr/bin/python3
def roman_to_int(roman_string):
    dico = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    num = 0

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            a = dico[roman_string[i]]
            b = dico[roman_string[i + 1]]
            if roman_string[i] in dico:
                if a < b:
                    num -= a
                else:
                    num += a
        else:
            num += dico[roman_string[i]]
    return num
