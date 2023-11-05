#!/usr/bin/python3
def no_c(my_string):

    new = ""
    for _ in my_string:
        if ord(_) == ord('c') or ord(_) == ord('C'):
            continue
        else:
            new += _
    return new
