#!/usr/bin/python3
import csv
import json
'''serealize and deserealize'''


def convert_csv_to_json(csv_filename):
    '''serealize and deserealize'''
    try:
        lst = []
        with open(csv_filename, 'r', encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for lines in reader:
                lst.append(lines)

        with open("data.json", 'w', encoding="utf-8") as json_file:
            json.dump(lst, json_file)

        return True
    except FileNotFoundError:
        return False
