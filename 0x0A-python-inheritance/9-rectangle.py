#!/usr/bin/python3
""" class BaseGeometry imported"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ Initialization """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area method implementation"""
        return self.__width * self.__height

    def str(self):
        """ str method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
