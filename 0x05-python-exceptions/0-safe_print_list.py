#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lenght = 0
    for number in range(x):
        try:
            print("{}".format(my_list[number]), end='')
            lenght += 1
        except IndexError:  # x can be bigger than the length of my_list
            continue  # this error is raised and continue with the exceptions
    print('')
    return lenght
