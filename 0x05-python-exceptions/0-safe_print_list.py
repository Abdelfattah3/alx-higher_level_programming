#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    i = 0
    try:
        for _ in my_list[:x]:
            print(_, end="")
            i += 1
    except IndexError:
        None
    print()
    return i
