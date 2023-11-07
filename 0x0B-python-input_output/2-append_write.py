#!/usr/bin/python3
'''this is a test'''


def append_write(filename="", text=""):
    '''this is a test'''
    with open(filename, "a", encoding="utf-8") as fil:
        return (fil.write(text))
