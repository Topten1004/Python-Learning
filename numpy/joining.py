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

a = np.random.rand(2, 3, 4)
b = np.random.rand(2, 3, 4)
c = np.concatenate((a, b), axis=2)

print(a)
print(b)
print(c)  # (2, 3, 8)