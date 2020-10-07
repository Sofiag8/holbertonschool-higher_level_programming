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
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
