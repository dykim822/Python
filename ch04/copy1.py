x = [2, 3, 5, 7, 11]
y = x   # 주소를 복사하기 때문에 값 또한 변경된다
k = list(x) # list함수를 사용하여 값을 복사해 새로운 list생성(k)
y[2] = 77
print(x)
print(y)
# 객체지향 의미!
print(k)