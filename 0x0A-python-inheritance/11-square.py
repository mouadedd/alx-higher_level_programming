#!/usr/bin/python3
'''this is a test'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''this is a test'''

    def __init__(self, size):
        '''this is a test'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' this is a test'''
        return self.__size ** 2

    def __str__(self):
        '''this is a test'''
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

