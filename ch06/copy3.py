import copy
a = [1, 2, 3]
x = [a, 100]
# deepcopy; 주소값에 해당하는 데이터까지 값을 복사
y = copy.deepcopy(x)    # 값을 복사
x[1] = 200
print(x)
print(y)
x[0][0] = 77
print(x)
print(y)