import numpy as np
ar1 = np.array([1,2,3]) # 1차원
ar2 = np.array([[1,2,3],[4,5,6]]) # 2차원 2행 3열
print(ar1)
print(ar2)
ar3 = np.arange(10)    # 0~9까지 1차원
print(ar3)
ar4 = ar3.reshape(2,5)
print(ar4)  # ar3를 2행 5열로 재구성
ar5 = np.linspace(0,1,6)    # start, end, num-points
print(ar5)
ar6 = np.linspace(0,1,5, endpoint=False)    # 마지막 제외
print(ar6)