#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for items in range(x):
        try:
            print("{:d}".format(my_list[items]), end='')
            num++
        except (ValueError, TypeError, IndexError):
            pass
        print()
        return num
