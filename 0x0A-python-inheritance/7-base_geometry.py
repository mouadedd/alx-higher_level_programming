#!/usr/bin/python3
'''this is a test'''


class BaseGeometry:
    '''this is a test'''
    def area(self):
i        '''this is a test'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' this is a test'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
