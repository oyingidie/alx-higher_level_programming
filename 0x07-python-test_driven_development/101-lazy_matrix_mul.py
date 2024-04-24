#!/usr/bin/python3
"""a function that multiplies two matrices using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """returns the multiplication of two matrices
    Args:
        m_a (int/float): the first list of lists
        m_b (int/float): the second list of lists
    """

    return (np.matmul(m_a, m_b))
