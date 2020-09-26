#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        exec = fct(*args)  # fct as a pointer to a function (div)
        return exec
        # due to task condition if something happens during the function
        # use Exception
        # All built-in,non-system exceptions are derived from this class
    except Exception as error:
        exec = None
        print("Exception: {}".format(error), file=stderr)
