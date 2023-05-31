#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for func in dir(hidden_4):
        if func[0] != "_":
            print("{}".format(func))
