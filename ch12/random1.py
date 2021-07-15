import numpy as np
print(np.random.normal(size=5)) # random 5개의 숫자 생성/ normal 정규분포
print(np.random.normal(size=(2,3)))
np.random.seed(seed=1)  # random하게 만들지만 한번 만든 숫자는 동일한 값으로 사용(잔류)
print(np.random.normal(size=5))