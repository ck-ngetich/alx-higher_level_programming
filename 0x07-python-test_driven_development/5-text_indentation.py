#!/usr/bin/python3
"""
Module text_indentation
Print  2  new lines after a set of characters.
"""

def text_indentation(text):

    """Prints text with added two newlines
    after each of these characters  {'.', '?', ':'}.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
