#!/usr/bin/python3
"""this is a test"""


def text_indentation(text):
    """this is a test"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    wild_c = ['.', '?', ':']
    n_text = ""
    for element in text:
        n_text += element
        if element in wild_c:
            n_text += "\n"
            print(n_text.strip(" "))
            n_text = ""
    if element not in wild_c:
        print(n_text.strip(" "), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
