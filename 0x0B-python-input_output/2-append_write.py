#!/usr/bin/python3
"""
Appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Adds a string to the end of a text file"""
    with open(filename, 'a', encodeing='utf-8') as f:
        f.write(text)
