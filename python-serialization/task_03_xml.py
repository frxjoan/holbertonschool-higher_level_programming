#!/usr/bin/python3
import xml.etree.ElementTree as ET
'''serealize and deserealize'''


def serialize_to_xml(dictionary, filename):
    '''serealize and deserealize'''
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    '''serealize and deserealize'''
    tree = ET.parse(filename)
    root = tree.getroot()

    res = {}
    for el in root:
        res[el.tag] = el.text
    return res
