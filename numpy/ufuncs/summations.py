import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)


import numpy as np

arr = np.array([1, 2, 3, 4])

newArr = np.cumsum(arr)

print(newArr)