import numpy as np
dat1 = [1,2,3,4,5]  # list
dat2 = [1,2,3,3.5,4]
arr1 = np.array(dat1)   # array로 변환(array가 속도가 더 빠르다)
print(arr1.shape)       # shape는 차원
arr2 = np.array(dat2)
print(arr2.shape)
print(arr1)
print(dat2)     # list는 정수, 실수 혼합되어 저장
print(arr2)     # 배열은 데이터형이 같은 형식으로 저장(모두 실수)
print(arr2.dtype)   # dtype은 데이터형
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])   # 2차원
print(arr3)
print(arr3.shape)   # 행, 열
print(len(arr3))    # 행의 갯수
print(len(arr3[0])) # 열의 갯수