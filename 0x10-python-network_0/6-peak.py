#!/usr/bin/python3
""" Peking method """


def find_peak(list_of_integers):
    """ find peak method in a list of unsorte integers
    Args:
    the integer list (list)
    This algorithm must have the lowest complexity
    """
    left = 0
    right = len(list_of_integers) - 1
    while left < right:
        mid = (left + (right - left)) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
        return left
