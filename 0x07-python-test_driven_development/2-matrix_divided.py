#!/usr/bin/python3


def matrix_divided(matrix, div):

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")

    if isinstance(matrix[0], list):
        lelem = len(matrix[0])

    for mat in matrix:
        if not isinstance(mat, list):
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")

        if len(mat) != lelem:
            raise TypeError("Each row of the matrix must have the same size")

        for elmnt in mat:
            if not isinstance(elmnt, (int, float)):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    n_matrix = [[round(idx / div, 2) for idx in mat] for mat in matrix]

    return n_matrix
