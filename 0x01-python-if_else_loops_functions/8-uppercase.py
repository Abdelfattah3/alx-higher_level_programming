#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            new += chr(ord(str[i]) - 32)
        else:
            new += str[i]
    print(new.format(new))
