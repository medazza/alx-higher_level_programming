#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for ind in range(0, list_length):
        try:
            new_list.append(my_list_1[ind] / my_list_2[ind])
        except TypeError:
            new_list.append(0)
            print("wrong type")
            continue
        except IndexError:
            new_list.append(0)
            print("out of range")
            continue
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
            continue
        finally:
            pass
    return new_list
