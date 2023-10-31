#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if str(a)+str(b) != "98":
            print("{:d}{:d}, ".format(a, b), end="")
        else:
            print("{:d}{:d}".format(a, b))
