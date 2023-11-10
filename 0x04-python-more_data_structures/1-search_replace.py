#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if not my_list:
        return None
    new_m = []
    for i in my_list:
        if i == search:
            new_m.append(replace)
        else:
            new_m.append(i)
    return new_m
