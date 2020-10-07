#!/usr/bin/python3
""" class BaseGeometry with public instance method """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ area method definition
        Raises:
            Exception: when area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method to validate value
        Args:
            name (str): first parameter
            value (int): second parameter to validate
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


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
