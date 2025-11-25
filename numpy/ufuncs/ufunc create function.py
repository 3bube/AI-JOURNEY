import numpy as np

def my_add(x, y):
    return x + y

my_add_ufunc = np.frompyfunc(my_add, 2, 1)

print(my_add_ufunc([1, 2, 3], [4, 5, 6]))
print(type(np.add))