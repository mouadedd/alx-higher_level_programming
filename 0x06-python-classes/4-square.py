#!/usr/bin/python3
'''define class'''


class Square:
    '''square attributes'''
    def __init__(self, size=0):
        '''init square'''
        self.size = size

    def area(self):
        '''the comment'''
        return (self.__size) ** 2

    @property
    def size(self):

        '''the comment'''
        return self.__size

    @size.setter
    def size(self, value):
        '''the comment'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
