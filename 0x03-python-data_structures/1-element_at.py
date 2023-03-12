#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if 0 <= idx and idx < size:
        return my_list[idx]
    return None
