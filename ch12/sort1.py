import numpy as np
x = np.array([4,2,6,5,1,3,0])
s1 = np.sort(x) # 본 데이터는 그대로이고 정렬된 결과만 s1에 저장
print(s1)
print(x)
x.sort()    # 원래 데이터를 정렬
print(x)