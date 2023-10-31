#!/usr/bin/python3
for _ in range(0, 100):
    if _ <= 98:
        print("{:02d}, ".format(_), end="")
    else:
        print("{:02d}".format(_))
