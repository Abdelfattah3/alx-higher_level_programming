#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    i = 0
    z = None
    for x, y in a_dictionary.items():
        if y > i:
            i = y
            z = x
    return z
