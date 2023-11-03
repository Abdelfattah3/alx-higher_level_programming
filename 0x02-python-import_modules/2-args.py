#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for _ in range(1, len(sys.argv)):
            print("{}: {}".format(_, sys.argv[_]))
