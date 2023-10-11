#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    diction = dict(a_dictionary)
    for key in a_dictionary:
        diction[key] = diction[key] * 2
    return diction
