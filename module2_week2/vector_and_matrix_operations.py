import numpy as np


# Length of a vector
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


# Dot product 
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


# Multiplying a vector by a matrix
def matrix_multi_vector(matrix, vector):
    result = vector * matrix
    return result


# Multiplying a matrix by a matrix
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


# Matrix inverse
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result
