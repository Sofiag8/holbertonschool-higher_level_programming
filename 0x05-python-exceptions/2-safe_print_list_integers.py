#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    lenght = 0
    for number in range(x):
        try:
            print("{:d}".format(my_list[number]), end='')
            lenght += 1
        except (TypeError, ValueError):  # other type & value skipped silently
            pass
    print('')
    return lenght
