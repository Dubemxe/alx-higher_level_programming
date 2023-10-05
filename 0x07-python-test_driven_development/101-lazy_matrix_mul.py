#!/usr/bin/python3
'''Defines a matrix multiplication function using NumPy'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''Return the multiplication of two matrices

    Args:
        m_a: the first matrix
        m_b: the second matrix
    '''
    return (np.matmul(m_a, m_b))
