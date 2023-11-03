#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) == 2:
        print("{}".format(int(sys.argv[1])))
    else:
        res = 0
        for _ in range(1, len(sys.argv)):
            res += int(sys.argv[_])
        print("{}".format(res, 'd'))
