#!/usr/bin/python3
'''this is a test'''


def inherits_from(obj, a_class):
    '''this is a test'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
