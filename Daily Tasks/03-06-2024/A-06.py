#How to inverse a matrix using NumPy

import numpy as np

matrix = np.array([[4, 7], [2, 6]])
inverse_matrix = np.linalg.inv(matrix)
print("Inverse of the matrix:")
print(inverse_matrix)
