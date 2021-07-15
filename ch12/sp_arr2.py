import numpy as np
b1 = np.zeros((2,3))    # 0으로 2행3열 채우기
print(b1)
b2 = np.ones_like(b1)   # b1과 같은 형식(2행3열)으로 1로 채우기
print(b2)
b3 = np.zeros_like(b1)  # b1과 같은 형식(2행3열)으로 0으로 채우기
print(b3)