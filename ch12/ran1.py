import numpy as np
a = np.random.normal(0,1,(2,3))
print(a)
data = np.random.normal(0,1,10000)
import matplotlib.pylab as plt
plt.hist(data, bins=100)    # bins 구간의 갯수
plt.show()