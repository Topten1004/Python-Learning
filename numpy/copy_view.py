import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 12

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()

arr[0] = 100

print(arr)
print(x)

# check with base

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

# copy return none
print(x.base)
# view returns original array
print(y.base)
