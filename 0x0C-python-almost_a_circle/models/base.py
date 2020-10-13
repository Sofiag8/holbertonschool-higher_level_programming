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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to JSON definition """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representatios to a file, definition """
        empty_list = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            empty_list = [x.to_dictionary() for x in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """ from JSON to string definition """
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)
