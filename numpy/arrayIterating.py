import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

# iterate on the elements of the following 2-D array:
for x in arr:
    print(x)

# iterate on each scalar element of the 2-D array
arr = np.array([[1,2,3], [4,5,6]])
for x in arr:
    for y in x:
        print(y)
        
# iterate on the elements of the following 3-D array

arr = np.array([[[1,2,3], [4,5,6],[7,8,9], [10,11,12]]])

for x in arr:
    print(x)

# iterate through teh following 3-D array:

arr = np.array([[[1,2], [3,4], [5,6], [7,8]]])

for x in np.nditer(arr):
    print(x)
    
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
  
arr = np.array([1,2,3])
for idx, x in np.ndenumerate(arr):
    print(idx,x)    
