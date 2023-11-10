#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda v: replace if v == search else v, my_list))
