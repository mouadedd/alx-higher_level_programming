#!/usr/bin/python3
'''this is a test'''


def read_file(filename=""):
    '''this is a test'''
    with open(filename, "r", encoding="utf-8") as fil:
        print(fil.read(), end="")
