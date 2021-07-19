import numpy as np
#             0  1  2  3
a = np.array([42,38,12,25])
j = np.argsort(a)
print(j)    # 작은 데이터가 있는 순서
print(a[j]) # 순서대로 출력해도 sort됨
i = j[::-1] # 순서를 거꾸로
print(i)
print(a[i]) # 큰 순으로 정렬
print(a[np.argsort(-a)])    # 큰 순으로 정렬, 내림차순