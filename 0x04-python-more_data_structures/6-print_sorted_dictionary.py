#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = dict(sorted(a_dictionary.items()))
    for i, x in a.items():
        print("{}: {}".format(i, x))
