#!/usr/bin/python3
import json
'''serealize and deserealize'''


def serialize_and_save_to_file(data, filename):
    '''serealize'''
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    '''deserealize'''
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
