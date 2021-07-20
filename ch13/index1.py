from pandas import Series, DataFrame
import pandas as pd
import numpy as np
items = {'code': [1,2,3,4,5,6],
 'name': ['apple','watermelon','oriental melon', 'banana', 'lemon', 'mango'],
 'manufacture': ['korea', 'korea', 'korea','philippines','korea', 'taiwan'],
 'price':[1500, 15000,1000,500,1500,700]}
data = DataFrame(items, columns=['code', 'name', 'manufacture', 'price'])
print(data)
data.index = np.arange(1,7,1)
print(data)
print(data.index)
data.price = [1500, 10000, 500, 1200, 300, 5000]
print(data)
data.price = Series([3000,20000,300,1000], index=[1,2,3,4])
print(data)
print(data.T)