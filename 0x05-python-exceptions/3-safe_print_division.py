#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:  # Raised when the second argument of div is zero
        result = None  # task condition
    finally:
        print("Inside result: {}".format(result), end='\n')
