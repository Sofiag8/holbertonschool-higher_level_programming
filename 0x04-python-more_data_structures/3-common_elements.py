#!/usr/bin/python3
def common_elements(set_1, set_2):
    return [common for common in set_1 for equal in set_2 if common is equal]
