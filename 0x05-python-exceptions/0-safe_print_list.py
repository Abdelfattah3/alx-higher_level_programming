#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    if not my_list or x <= 0:
        return 0
    try:
        i = 0
        for _ in my_list[:x]:
            print(_, end="")
            i += 1
            if i == x or _ == my_list[-1]:
                print()
        return i
    except IndexError:
        return i
