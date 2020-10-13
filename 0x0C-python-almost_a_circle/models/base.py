#!/usr/bin/python3
""" first class Base """
import json


class Base:
    """ Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ to JSON definition """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
