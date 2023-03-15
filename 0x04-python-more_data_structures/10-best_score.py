#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        mx = max(list(a_dictionary.values()))
        for key in a_dictionary.keys():
            if mx == a_dictionary[key]:
                return key
    except AttributeError:
        pass
    return None
