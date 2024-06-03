#Find the number of rows and columns of a given matrix using NumPy

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
rows, cols = matrix.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
