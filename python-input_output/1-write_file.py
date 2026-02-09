#!/usr/bin/python3
'''write file'''


def write_file(filename="", text=""):
    '''write in file'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
