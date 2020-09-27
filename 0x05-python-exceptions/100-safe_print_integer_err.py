#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
        # specify built-in Exception to make alias
    except Exception as error:
        # therefore more readable instead of sys.exc_info()[1])
        print("Exception: {}".format(error), file=stderr)
        return False
