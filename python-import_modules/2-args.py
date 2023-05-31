#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    if (len(sys.argv) == 1):
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        print("{} argument{}:".format(len(sys.argv) -
              1, "s" if len(sys.argv) != 2 else ""))
    for arguments in sys.argv[1:]:
        print("{}: {}".format(i, arguments))
        i += 1
