#!/usr/bin/python3
for _ in range(122, 96, -1):
    if _ % 2 != 0:
        _ -= 32
    print("{}".format(chr(_)), end="")
