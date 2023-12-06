#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n__matrix = matrix.copy()

    for x in range(len(matrix)):
        n__matrix[x] = list(map(lambda n: n**2, matrix[x]))

    return (n__matrix)
