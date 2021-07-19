import numpy as np
a = np.array([[4,3,5,7],[1,12,11,9],[2,15,1,14]])
print(a)
print(np.sort(a, axis=1)) # axis = 1, axis=-1, 행 정열
print(np.sort(a, axis=0))