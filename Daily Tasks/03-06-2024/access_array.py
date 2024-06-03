import numpy as np
#created an array
array_2D = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)

#accessing a single element
element = array_2D[1,2]
print(element)

print("element at the index of [0,1]", element)

#Access by 2 row
row = array_2D[1:]
print("Second row : ", row)

# Access the second column
column = array_2D[:, 1]
print("Second column:", column)

