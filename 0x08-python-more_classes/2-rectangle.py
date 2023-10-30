#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""


class Rectangle:
    """
    Defines class rectangle
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Initialize the rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter, sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets the height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ width*2 + height*2 """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)
