#!/usr/bin/python3
'''this is a test'''


class Student:
    '''this is a test'''

    def __init__(self, first_name, last_name, age):
        '''this is a test'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''this is a test'''
        if (type(attrs) == list and all(
                type(elem) == str for elem in attrs)):
            return {dic: getattr(self, dic) for dic
                    in attrs if hasattr(self, dic)}
        return self.__dict__

    def reload_from_json(self, json):
        '''this is a test'''
        for dic, i in json.items():
            setattr(self, dic, i)
