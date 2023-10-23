#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for ind in range(0, list_length):
        try:
            div = my_list_1[ind] / my_list_2[ind]
        except TypeError:
            print("Wrong type")
            div = 0
            new_list.append(div)
            continue
        except IndexError:
            print("Out of range")
            div = 0
            new_list.append(div)
            continue
        except ZeroDivisionError:
            print("Division by 0")
            div = 0
            new_list.append(div)
            continue
        finally:
            new_list.append(div)
    return new_list
