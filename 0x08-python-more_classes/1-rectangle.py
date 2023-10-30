#!/usr/bin/python3
"""task 1 Module for the rectangle """


class Rectangle:
    """class for the rectangle"""
    def __init__(self, width=0, height=0):
        """  getter and setter's initalize values
        Args:
            width(int) = rectangle width
            height(int) = rectangle height
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter - allows to get width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter- sets the width
            Args:
                value(int): the value setted as width
            """

            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise TypeError("width must be >= 0")

            self.__width = value

        @property
        def height(self):
            """Getter - gets height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter- sets height value
           Args:
                value(int): value setted as height
            """

            if type(value) != int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")

            self.__height = value
