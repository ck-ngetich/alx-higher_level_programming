#!/usr/bin/python3

"""Module matrix_mul
Multiplies two matrices .
"""

def matrix_mul(m_a, m_b):
    """Give  matrix resulting of
    the multiplication of m_a and m_b.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    x = len(m_a)
    if x == 0:
        raise ValueError("m_a can't be empty")
    y = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if y is None:
            y = len(i)
            if y == 0:
                raise ValueError("m_a can't be empty")
        if y != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    z = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if z is None:
            z = len(i)
            if z == 0:
                raise ValueError("m_b can't be empty")
        if z != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if y != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(x):
        l = []
        for j in range(z):
            n = 0
            for k in range(y):
                n += m_a[i][k] * m_b[k][j]
            l.append(n)
        matrix.append(l)
    return matrix
