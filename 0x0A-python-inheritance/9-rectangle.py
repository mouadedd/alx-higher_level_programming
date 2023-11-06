#!/usr/bin/python3
'''this is a test'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''this is a test'''

    def __init__(self, width, height):
        '''this is a test'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''this is a test'''
        return self.__width * self.__height

    def __str__(self):
        '''this is a test'''
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
