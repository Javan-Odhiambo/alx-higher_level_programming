#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    try:
        for i, _ in enumerate(matrix):
            c = 0
            for j, v in enumerate(matrix[i][:-1]):
                print("{:d}".format(v), end=" ")
                c = j
            c = 0 if len(matrix[0]) == 1 else c +1
            print("{:d}".format(matrix[i][c]))
    except IndexError:
        print("")
