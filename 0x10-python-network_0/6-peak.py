#!/usr/bin/python3
"""Func that defines a peak-finding algorithm."""


def find_peak(list_of_ints):
    """Return the  peak in a list of unsorted ints."""
    if list_of_ints == []:
        return None

    size = len(list_of_ints)
    if size == 1:
        return list_of_ints[0]
    elif size == 2:
        return max(list_of_ints)

    mid = int(size / 2)
    peak = list_of_ints[mid]
    if peak > list_of_ints[mid - 1] and peak > list_of_ints[mid + 1]:
        return peak
    elif peak < list_of_ints[mid - 1]:
        return find_peak(list_of_ints[:mid])
    else:
        return find_peak(list_of_ints[mid + 1:])
