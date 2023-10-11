#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_rem = list(a_dictionary.keys())
    for elem in keys_to_rem:
        if value == a_dictionary.get(elem):
            del a_dictionary[elem]
    return (a_dictionary)
