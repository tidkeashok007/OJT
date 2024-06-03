#Calculate the sum of the diagonal elements of a NumPy array 33 and 44

import numpy as np

array_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_diagonal_3x3 = np.trace(array_3x3)
print("Sum of diagonal elements of a 3x3 array:", sum_diagonal_3x3)

array_4x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
sum_diagonal_4x4 = np.trace(array_4x4)
print("Sum of diagonal elements of a 4x4 array:", sum_diagonal_4x4)
