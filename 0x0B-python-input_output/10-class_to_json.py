#!/usr/bin/python3
""" JSON serialization of an object """
import json


def class_to_json(obj):
    """ definition """
    return obj.__dict__
