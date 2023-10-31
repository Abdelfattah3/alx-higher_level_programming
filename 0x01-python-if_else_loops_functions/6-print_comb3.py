#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a != b and a < b:
            if str(a) + str(b) != '89':
                print("{:d}{:d}, ".format(a, b), end="")
            else:
                print("{:d}{:d}".format(a, b))
        else:
            continue
