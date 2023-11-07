#!/usr/bin/python3
'''this is a test'''


def write_file(filename="", text=""):
    '''this is a test'''
    with open(filename, "w", encoding="utf-8") as fil:
        return (fil.write(text))
