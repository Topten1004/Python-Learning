# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr.dtype)

stringArr = np.array(['apple', 'banana', 'cherry'])

print(stringArr.dtype)

arr = np.array([1,2,3,4], dtype='S')

print(arr)
print(arr.dtype)

# set datatype
arr = np.array([1,2,3,4], dtype='i4')

print(arr)
print(arr.dtype)

# convert datatype float to int
arr = np.array([1.2, 2.3, 3.5, 4.5])

newarr = arr.astype('i')

print(newarr)

print(newarr.dtype)

# convert float type to int type
arr = np.array([1.1, 2.1, 5.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

# convert data type from integer to boolean
arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
