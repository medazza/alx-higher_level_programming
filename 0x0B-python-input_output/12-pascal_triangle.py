#!/usr/bin/python3
"""Module contains pasacal triangle func that create list of lists """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    
    triangles = []
    l = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(l[j] + l[j - 1])
        l = row
        triangles.append(row)
    return (triangles)
