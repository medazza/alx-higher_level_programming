#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ind = 0
    while ind < x:
        try:
            print(my_list[ind], end="")
        except IndexError:
            break
        ind += 1
    print("")
    return ind
