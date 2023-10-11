#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_list = set(my_list)
    total = 0
    for item in unique_list:
        total += item
    return (total)
