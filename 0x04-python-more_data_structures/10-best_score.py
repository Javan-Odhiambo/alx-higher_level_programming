#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        return max(list(a_dictionary.keys()))
    except AttributeError:
        return None
