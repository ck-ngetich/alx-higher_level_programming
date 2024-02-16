#!/usr/bin/python3
"""
matrix_divided divides the given matrix by the parameter and returns the divided one
"""
def matrix_divided(matrix, div):
    """
    Checks if the entire list isint/float
    Checks if each list of the matrices have the same size
    checks if "div" is an int/float or is 0
    """
    matrix_res= []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                inner_list.append(round(items / div, 2))
        matrix_res.append(inner_list)

    return matrix_res
