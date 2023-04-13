#!/usr/bin/python3
"""
Opening a file and writing to it

"""


def write_file(filename="", text=""):
    """Reading the file using with"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
