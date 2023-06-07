#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    errors = 0
    for i in range(0, x + 1):
        try:
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            errors += 1
            continue
        except TypeError:
            errors += 1
            continue
        except IndexError:
            print()
            return i - errors
    print()
    return i - errors
