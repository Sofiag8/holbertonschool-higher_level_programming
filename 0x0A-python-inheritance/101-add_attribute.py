#!/usr/bin/python3


def add_attribute(object, name, value):
    """ method """
    if hasattr(object, "__dict__"):  # hasattr check in object has attributes
        setattr(object, name, value)
    else:
        raise TypeError("can't add new attribute")
