"""[numpy]
- linear algebra library

"""

import numpy as np 

nrow = 2
ncol = 10
numList = np.random.uniform(0, 100, size = (nrow, ncol))
print(numList)

arr = np.array(numList)
print(arr)

print("Min : ", np.min(arr))
print("Max : ", np.max(arr))
print("Mean: ", np.mean(arr))
print("SUM : ", np.sum(arr))
print("STD : ", np.std(arr))
print("VAR : ", np.var(arr))

print(arr >= np.mean(arr))