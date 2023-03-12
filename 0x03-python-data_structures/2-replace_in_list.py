#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    size = len(my_list)
    if 0 <= idx and idx < size:
        my_list[idx] = element
    return my_list
