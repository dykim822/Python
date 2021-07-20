from pandas import Series, DataFrame
items = {'1':{'name':'apple', 'manufacture':'korea', 'price':1500},
 '2': {'name': 'watermelon', 'manufacture': 'korea', 'price': 15000},
 '3': {'name': 'oriental melon', 'manufacture': 'korea', 'price': 1000},
 '4': {'name': 'banana', 'manufacture': 'philippines', 'price': 500},
 '5': {'name': 'lemon', 'manufacture': 'korea', 'price': 1500},
 '6': {'name': 'mango', 'manufacture': 'korea', 'price': 700}}
data = DataFrame(items)
data = data.T
print(data)
data = data.drop("1") # "1"행 삭제
print(data)
data = data.drop(["3","5"]) # "1"행 삭제
print(data)
data = data.drop("price",axis=1) # "price"컬럼 삭제
print(data)