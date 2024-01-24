#!/usr/bin/python3
"""this is a test"""


def text_indentation(text):
    """this code print a text with a break after each wild card('.' '?' ':')
    except for the last line"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    wildo = ['.', '?', ':']
    ness = ""
    for c in text:
        ness += c
        if c in wildo:
            ness += "\n"
            print(ness.strip())
            print()
            ness = ""
    if c not in wildo:
        print(ness.strip(), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
