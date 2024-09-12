#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = sys.argv.__len__()
    nArgMsg = "argument"

    if argc != 1:
        nArgMsg += 's'

    if argc == 0:
        nArgMsg += "."
    else:
        nArgMsg += ":"

    print("{:d} ".format(argc-1) + nArgMsg)

    for arg in range(1, argc):
        print("{:d}: {}".format(arg, sys.argv[arg]))
