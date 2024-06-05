import numpy as np
#for-in loop
#1d array
array_1D = np.array([1,2,3,4,5,6])

#iterate the elements in this array
print("Array_1d :",array_1D)

for elements in array_1D:
     print(elements)

array_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D array :",array_2D)


for elements in array_2D:
     print(elements)

#nested loop
for row in array_2D:
     for elements in row:
          print(elements)
          
for elements in np.nditer(array_2D):
     print(elements)

#iterate the elements with index
for inex, element in np.ndenumerate(array_2D):
     print(f"index: {index}, Element : {element}")