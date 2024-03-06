#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_del = []
    for key, v in a_dictionary.items():
        if v == value:
            key_to_del.append(key)
    for key in key_to_del:
        del a_dictionary
    return (a_dictionary)
