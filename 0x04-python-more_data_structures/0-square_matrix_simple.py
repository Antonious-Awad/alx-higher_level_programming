#!/usr/bin/python3
def square_matrix_simple(matrix: list = []):
    new_matrix = matrix.copy()
    for i in new_matrix:
        for j in i:
            j = j**2
    return new_matrix
