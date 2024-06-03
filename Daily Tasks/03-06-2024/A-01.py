#Counts the number of non-zero values in the array

import numpy as np

array = np.array([1, 0, 5, 0, 3, 2, 0])
count_nonzero = np.count_nonzero(array)
print("Number of non-zero values:", count_nonzero)
