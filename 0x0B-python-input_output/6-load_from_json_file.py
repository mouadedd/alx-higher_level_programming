#!/usr/bin/python3
'''this is a test'''
import json


def load_from_json_file(filename):
    '''this is a test'''
    with open(filename, "r", encoding="utf-8") as fil:
        return json.load(fil)
