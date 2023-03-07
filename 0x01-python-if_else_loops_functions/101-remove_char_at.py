#!/usr/bin/python3
def remove_char_at(str, n):
    p = [v for i, v in enumerate(str) if i != n]
    return "".join(p)
