#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_rem = []
    for key in a_dictionary:
        if a_dictioanry[key] == value:
            keys_rem.append(key)
    for key in keys_rem:
        del a_dictionary[key]
    return a_dictionary
