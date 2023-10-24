#!/usr/bin/python3
''' define class'''


class Square:
    '''class attribut'''
    def __init__(self, size=0):
        ''' int class'''
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        ''' parameter of square'''
        return self.__size ** 2
