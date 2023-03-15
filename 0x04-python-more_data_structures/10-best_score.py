#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        try:
            return max(list(a_dictionary.keys()))
        except AttributeError:
            pass
    return None
