#!/usr/bin/python3
'''this is a test'''


class Student:
    '''this is a test'''
    def __init__(self, first_name, last_name, age):
        '''this is a test'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''this is a test'''
        return self.__dict__
