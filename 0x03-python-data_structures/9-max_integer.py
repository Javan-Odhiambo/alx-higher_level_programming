#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        max = None

    max = my_list[0]
    for i in my_list[1:]:
        if i > max:
            max = i

    return max
