#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for i in my_list:
            max = i if i > max else max
    else:
        max = None

    return max
