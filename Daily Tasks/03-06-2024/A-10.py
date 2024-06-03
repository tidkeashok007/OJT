#How to count the frequency of unique values in NumPy array?


import numpy as np

array = np.array([1, 2, 3, 4, 1, 2, 1, 3, 4, 1])
unique_values, counts = np.unique(array, return_counts=True)
print("Unique values:", unique_values)
print("Counts:", counts)
