import pandas as pd
items1 = {'1':{'price':1500},
 '2': {'price': 15000},
 '3': {'price': 1000}}
items2 = {'1':{'price':1500},
 '2': {'price': 15000},
 '4': {'price': 1000}}
data1 = pd.DataFrame(items1)
data1 = data1.T
data2 = pd.DataFrame(items2)
data2 = data2.T
print(data1)
print(data2)
print(data1+data2)
print(data1.add(data2, fill_value=0))