import numpy as np

arr = np.array([1,2,3,4,4,5,6])

x = np.where(arr == 4)

print(x)

arr = np.array([1,2,3,4,5,6,7,8])

x = np.where(arr %2 == 0)

print(x)

x = np.where( arr % 2 == 1)

print(x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

# 1 2 3 5 7 [1]
# 1 3 4 5 7 [2]
# 1 3 5 6 7 [3]
print(x)

