#Adding and Subtracting Matrices in Python.

import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Addition
addition_result = np.add(matrix1, matrix2)
print("Matrix Addition Result:")
print(addition_result)

# Subtraction
subtraction_result = np.subtract(matrix1, matrix2)
print("\nMatrix Subtraction Result:")
print(subtraction_result)
