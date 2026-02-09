#!/usr/bin/python3
import pickle
'''serealize and deserealize'''


class CustomObject:
    '''serealize and deserealize'''

    def __init__(self, name, age, is_student):
        '''serealize and deserealize'''
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''serealize and deserealize'''
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        '''serealize and deserealize'''
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        '''serealize and deserealize'''
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (pickle.UnpicklingError, EOFError, FileNotFoundError):
            return None
