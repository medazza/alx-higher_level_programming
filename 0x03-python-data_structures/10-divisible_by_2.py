#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Function that find all multiples of 2 in a list."""
    list_mult = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_mult.append(True)
        else:
            list_mult.append(False)
    return (list_mult)
