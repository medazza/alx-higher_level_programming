#!/usr/bin/python3
"""Module for matrix_mul method (func)."""


def matrix_mul(m_a, m_b):
    """Func that  multiplies one matrix by another.
    Args:
        m_a: First matrix
        m_b: Second matrix
    Returns:
        matrix: The product result.
    Raises:
        TypeError: If m_a or m_b arn't lists.
        TypeError: If m_a or m_b arn't lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int or float.
        TypeError: If m_a or m_b arn't rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_empty = False
    m_b_empty = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False
    for r in m_a:
        if not isinstance(r, list):
            raise TypeError("m_a must be a list of lists")
        if len(r) != len(m_a[0]):
            m_a_notrect = True
        for n in r:
            if not isinstance(n, (int, float)):
                m_a_notnum = True

    for r in m_b:
        if not isinstance(r, list):
            raise TypeError("m_b must be a list of lists")
        if len(r) != len(m_b[0]):
            m_b_notrect = True
        for n in r:
            if not isinstance(n, (int, float)):
                m_b_notnum = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notnum:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_notrect:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_notrect:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            result[i].append(c)

    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
