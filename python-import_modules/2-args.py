#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    print("{} arguments.".format(len(sys.argv) - 1))
    for arguments in sys.argv[1:]:
        print("{}: {}".format(i, arguments))
        i += 1
