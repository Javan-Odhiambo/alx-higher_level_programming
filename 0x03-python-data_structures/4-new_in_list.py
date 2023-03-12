#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    if 0 <= idx and idx < size:
        my_list = [v if i != idx else element for i, v in enumerate(my_list)]
    return my_list
