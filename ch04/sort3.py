# sort: 데이터 변경됨/ sorted: 데이터 변경 X
# 대소문자 구별 & 소문자가 대문자가 크다
data = ['Morining', 'Afternoon', 'evening', 'Night']
data.sort()
print(data)
data.sort(reverse=True)
print(data)
# 대소문자 구별없이 정렬
data.sort(key=str.lower)
print(data)
data.sort(key=str.lower, reverse=True)
print(data)