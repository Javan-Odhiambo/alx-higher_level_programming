#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if 0 <= idx and idx < size:
        my_list.remove(my_list[idx])
    return my_list