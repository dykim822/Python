import numpy as np
a = np.array([10,20,30])
b = np.arange(12).reshape((4,3))
print(a)
print(b)
print(a + b) # a가 4행 3열로 변경되어 연산과 같은 효과
print(b+10) # 배열이 아닌 값을 스칼라, 각 항에 연산