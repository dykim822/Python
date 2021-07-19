from pandas import Series, DataFrame
items = {'code': [1,2,3,4,5,6],
 'name': ['apple','watermelon','oriental melon', 'banana', 'lemon', 'mango'],
 'manufacture': ['korea', 'korea', 'korea','philippines','korea', 'taiwan'],
 'price':[1500, 15000,1000,500,1500,700]}
data = DataFrame(items, columns=['code', 'name', 'manufacture', 'price'])
print(data)
print(data['name']) # 컬럼이 name
print(data._ixs(0)) # 0번 인덱스 데이터
print(data['name'][0])