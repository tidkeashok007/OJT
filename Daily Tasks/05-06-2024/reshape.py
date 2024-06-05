#converting 1D Into 2D
#.reshape() is the method which is used for reshaping 
import numpy as np

#create a 1D array 
array_1D = np.array([1,2,3,4,5,6])
print("array1D : ",array_1D)
print("shape of array1D : ",array_1D.shape)

#reshape the 1D arrayb to 2D array
array_2D = array_1D.reshape((2,3))
print("2D array : ",array_2D)
print("shape of array_2D ",array_2D.shape)

#reshape the 2D array to 1D array
array_1D_back = array_2D.reshape(-1)
print("1D array back ", array_1D_back)
print("shape of array_1D_back ",array_1D_back.shape)

#reshape 1D array into 3D array
array_3D = array_1D.reshape((3,2))
print("3D_array ",array_3D)
print("shape of the array ",array_3D.shape)

