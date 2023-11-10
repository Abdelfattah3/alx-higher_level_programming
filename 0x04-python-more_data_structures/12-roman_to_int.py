#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    x = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    no = 0
    to = 0
    for r in reversed(roman_string):
        no = x[r]
        to += no if to < no * 5 else -no
    return to
