#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        mod_string_zero = my_string.translate({ord('c'): None})
        mod_string_one = mod_string_zero.translate({ord('C'): None})
        return (mod_string_one)
    else:
        return (my_string)
