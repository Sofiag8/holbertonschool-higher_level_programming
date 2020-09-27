#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError()  # force a specified exception to occur
    except TypeError:
        raise
