from pandas import Series, DataFrame
items = {'1':{'name':'apple', 'manufacture':'korea', 'price':1500},
 '2': {'name': 'watermelon', 'manufacture': 'korea', 'price': 15000},
 '3': {'name': 'oriental melon', 'manufacture': 'korea', 'price': 1000},
 '4': {'name': 'banana', 'manufacture': 'philippines', 'price': 500},
 '5': {'name': 'lemon', 'manufacture': 'korea', 'price': 1500},
 '6': {'name': 'mango', 'manufacture': 'korea', 'price': 700}}
data = DataFrame(items)
data = data.T # 행과 열 교환
print(data)
# 6번은 없어지고 7번이 추가 됬는데 값은 NaN
data1 = data.reindex(['1','2','3','4','5','7'])
print(data1)
# 6번은 없어지고 7번이 추가 됬는데 값은 0
data1 = data.reindex(['1','2','3','4','5','7'], fill_value=0)
print(data1)
# 6번은 없어지고 7번이 추가 됬는데 값은 0
data1 = data.reindex(['1','2','3','4','5','7'], method='ffill')
print(data1)