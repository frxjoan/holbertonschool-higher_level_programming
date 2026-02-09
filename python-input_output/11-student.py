#!/usr/bin/python3
'''json file'''


class Student:
    '''json class trust'''
    def __init__(self, first_name, last_name, age):
        '''json file'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''json file'''
        if attrs is None:
            return self.__dict__
        else:
            dico = {}
            for el in attrs:
                if el in self.__dict__:
                    dico[el] = self.__dict__[el]
            return dico

    def reload_from_json(self, json):
        '''json file'''
        for key in json.keys():
            setattr(self, key, json[key])
