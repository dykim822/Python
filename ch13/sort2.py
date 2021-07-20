import pandas as pd
items = {'apple':{'count':10,'price':1500},
 'banana': {'count':5, 'price': 15000},
 'melon': { 'count':7,'price': 1000},
 'kiwi': {'count':20,'price': 500},
 'mango': {'count':30,'price': 1500},
 'orange': { 'count':4,'price': 700}}
data = pd.DataFrame(items).T
print(data)
# 가격이 내림차순이고 가격이 같으면 count가 작은 순
print(data.sort_values(ascending=[False, True], by=['price','count']))
print(data.rank())
# 큰 순서대로 번호 부여
print(data.rank(ascending=False, method='min'))