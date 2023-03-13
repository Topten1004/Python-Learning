import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])

print(arr.shape)

# create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimensions has value 4
arr = np.array([[1,2,3,4], [5,6,7,8]])

print(arr.shape)


# create an array with 5 dimensions
arr = np.array([1,2,3,4], ndmin=4)

print(arr)
print('shape of array : ', arr.shape)