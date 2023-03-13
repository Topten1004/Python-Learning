import numpy as np

arr = np.array([1,2,5,4,3])

x = [True, False, False,True, False]

newarr = arr[x]

print(newarr)

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)