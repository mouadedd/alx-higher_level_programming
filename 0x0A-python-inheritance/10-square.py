#!/usr/bin/python3i
'''this is a test'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''this is a test'''

    def __init__(self, size):
        '''this is a test'''
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        '''this is a test'''
        return self.__size ** 2
