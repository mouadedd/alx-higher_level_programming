#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """class for the rectangle"""
    def __init__(self, width=0, height=0):
        """ class argement
            width(int) = rectangle width
            height(int) = rectangle height
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter - allows to gets width value"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter- sets the value of width
            Args:
                value: the value to set to width
            """

            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise TypeError("width must be >= 0")

            self.__width = value

        @property
        def height(self):
            """Getter - allows to get height"""
            return self.__height

        @height.setter
        def height(self, value):
            """ sets the value of height
           Args:
                value: the value to set to height
            """

            if type(value) != int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")

            self.__height = value
