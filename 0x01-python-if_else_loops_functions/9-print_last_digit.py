#!/usr/bin/python3
def print_last_digit(number):
    temp = number if number > 0 else number * -1
    last = temp % 10 if number > 0 else (temp % 10)
    print("{}".format(last), end="")
    return last