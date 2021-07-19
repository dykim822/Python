import numpy as np
ar = np.arange(30)
print(ar)
np.savetxt('test.csv', ar)  # csv로 저장
br = np.loadtxt('test.csv', delimiter='\t')
print(br)