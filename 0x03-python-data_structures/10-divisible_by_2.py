#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    if not my_list:
        return None
    list_res = []
    for x in my_list:
        if my_list[x] % 2 == 0:
            list_res.append(True)
        else:
            list_res.append(False)
    return list_res
