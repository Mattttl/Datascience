import numpy as np

A = np.arange(9,dtype=np.float64).reshape(3,3)
B = np.array([10,10,10])
print(np.add(A,B)) 
# Concat
C = np.array([11,11,11])
print(np.concatenate((B,C)))