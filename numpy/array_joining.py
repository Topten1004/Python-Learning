import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.concatenate([arr1, arr2])

print(arr)

# Join two 2-D arrays along rows (axis = 1)

arr1 = np.array([[1,2], [3,4], [5,6]])
arr2 = np.array([[7,8], [9,10], [11,12]])

arr = np.concatenate((arr1, arr2), axis = 0)

print(arr)

a = np.array([[1,2,3,4],[5,6,7,8], [9,10,11,12],[13,14,15,16]])
b = np.array([[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32]])
c = np.concatenate((a, b), axis=1)
print(a)
print(b)
print(c)
# Joining Arrays using Stack functions
arr = np.stack((a,b), axis=0)
print(arr)

# Stacking Along Rows
arr = np.hstack((arr1, arr2))
print(arr)

# Stacking Along Columns
arr = np.vstack((arr1, arr2))
print(arr)

# Stacking Along Height(Depth)
arr = np.dstack((arr1, arr2))
print(arr)