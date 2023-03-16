#!/usr/bin/python3
def weight_average(my_list=[]):
    results = 0
    if my_list:
        results = (sum([x[0] * x[1] for x in my_list]) /
                   sum([x[1] for x in my_list]))
    return results
