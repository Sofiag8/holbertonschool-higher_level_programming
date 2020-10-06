#!/usr/bin/python3
""" Class MyList inherit from list"""


class MyList(list):
    def print_sorted(self):
        """ public instance method definition
        prints a sorted list (ascending sort)
        """
        print(sorted(self))
