import pandas as pd
items = {'apple':{'count':10,'price':1500},
'banana': {'count':5, 'price': 15000},
'melon': { 'count':7,'price': 1000},
'kiwi': {'count':20,'price': 500},
'mango': {'count':30,'price': 1500},
'orange': { 'count':4,'price': 700}}
data = pd.DataFrame(items).T
print(data)
data.to_csv("data.csv", index=False, header=False)