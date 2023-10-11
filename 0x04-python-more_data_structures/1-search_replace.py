#!/usr/bin/python3
def search_replace(my_list, search, replace):
    the_list = my_list[:]
    for e in range(len(the_list)):
        if the_list[e] == search:
            the_list[e] = replace
    return the_list
