#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    i = x = 0
    while i < list_length:
        try:
            new_list += [my_list_1[x] / my_list_2[x]]
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            x += 1
            i += 1
    return new_list
