#!/usr/bin/python3
""" class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def __str__(self):
        """ string representation """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
