#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary
    for key in a_dictionary.keys():
        if new[key] == value:
            new.pop(key)
    return new
