import numpy as np

arr = np.array([10, 15, 25, 5])

print(np.diff(arr, n=2))  # Output: [ 5 10 -20]