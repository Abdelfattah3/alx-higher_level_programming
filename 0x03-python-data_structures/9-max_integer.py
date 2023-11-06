#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None

    a = my_list[0]
    for x in range(1, len(my_list)):
        if my_list[x] > a:
            a = my_list[x]
    return a
