#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
# returns a new matrix with squared input
    squared_matrix = [[x ** 2 for x in row] for row in matrix]
    return (squared_matrix)
