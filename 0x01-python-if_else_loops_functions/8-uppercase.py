#!/usr/bin/python3
def uppercase(str):
    strcpy = ""
    for c in str:
        n = ord(c)
        if n >= 97 and n <= 122:
            strcpy += chr(n-32)
        else:
            strcpy += c
    print("{}".format(strcpy))
