#!/usr/bin/python3
'''this is a test'''
import json


def save_to_json_file(my_obj, filename):
    '''this is a test'''
    with open(filename, "w", encoding="utf-8") as fil:
        json.dump(my_obj, fil)
