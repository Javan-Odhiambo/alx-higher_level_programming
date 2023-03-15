#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    for key in a_dictionary.keys():
        result[key] = a_dictionary[key] * 2
    return result
