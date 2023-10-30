#!/usr/bin/python3
""" define rectangle """


class Rectangle:
    """class of  rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """print string if a instance  is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """get width's value"""
        return self.__width

    @width.setter
    def width(self, value):
        """set for width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """width*2 + height*2 or 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """visual representation"""
        strg = ""
        if self.__width != 0 and self.__height != 0:
            strg += "\n".join(str(self.print_symbol) * self.__width
                                for elem in range(self.__height))
        return strg

    def __repr__(self):
        """string representation o"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
