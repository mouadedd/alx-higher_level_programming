#!/usr/bin/python3
'''defining a class square'''


class Square:
    '''mandatory comment'''
    def __init__(self, size=0):
        '''mandatory comment'''
        self.size = size

    def area(self):
        '''mandatory comment'''
        return (self.__size) ** 2

    @property
    def size(self):
        '''mandatory comment'''
        return self.__size

    @size.setter
    def size(self, value):
        '''mandatory comment'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        '''mandatory comment'''
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
