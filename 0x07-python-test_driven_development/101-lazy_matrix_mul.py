#!/usr/bin/python3
"""
This module multiply 2 matrix using numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Func multiply 2 matrix that is given
    Args:
        m_a: input first matrix
        m_b: input second matrix
    Returns:
        return m_a * m_b
    """
    return np.matmul(m_a, m_b)
