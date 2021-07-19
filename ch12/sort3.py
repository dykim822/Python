import numpy as np
ar = np.array([[3,8,2],[9,1,4],[6,7,3]])
print(ar)
print(np.sort(ar, axis=0))  # 열 정렬
print(np.sort(ar, axis=0)[::-1])    # 열 내림차순
print(np.sort(ar, axis=1))  # 행 정렬
print(np.sort(ar, axis=1)[:,::-1])  # 행 역순 정렬