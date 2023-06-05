#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    iterator = ['a', 'b']
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    for z in iterator:
        if len(eval("list_" + z)) < 2:
            for i in range(len(eval("list_" + z)), 2):
                eval("list_" + z).append(0)
    return (list_a[0] + list_b[0], list_a[1] + list_b[1])
