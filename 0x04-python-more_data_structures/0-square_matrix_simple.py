#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for num_list in matrix:
        result.append(list(map(lambda x: x * x, num_list)))
    return result
