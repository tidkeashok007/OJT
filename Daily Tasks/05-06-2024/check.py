import numpy as np
array = np.array([10,20,12,15,17])
#np.where(array == 20)
#where(): use to check the particular condition

elements = np.where(array>15)
print(array[elements])