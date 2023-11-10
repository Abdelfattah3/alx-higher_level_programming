#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if str(key) in a_dictionary:
        del a_dictionary[str(key)]
        return a_dictionary
    return a_dictionary
