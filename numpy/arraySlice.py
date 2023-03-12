import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr[1:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

print(arr[4:])

#negative slice
print(arr[-3:-1])

# print items by interval 3
print(arr[1:6:3])

# return every items by interval
print(arr[::2])

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# multiple dimension array
print(arr[1, 1:4])

# return index both arrays
print(arr[0:2, 3])

# from both elements, slice index 1 to index 4 (not included), this will return a 2-D array
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# from both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print(arr[0:2, 1:4])

