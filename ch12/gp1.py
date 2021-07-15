import numpy as np
# ar1 = np.linspace(0,1,5)
ar1 = np.logspace(0.1,1,20, endpoint=True)
print(ar1)
import matplotlib.pyplot as plt
plt.plot(ar1, 'o')  # 동그라미 형식으로 좌표찍기
plt.show()