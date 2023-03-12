#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    try:
        for i, _ in enumerate(matrix):
            c = 0
            for j, v in enumerate(matrix[i][:-1]):
                print("{:d}".format(v), end=" ")
                c = j
            print("{:d}".format(matrix[i][c+1]))
    except IndexError:
        print("")
