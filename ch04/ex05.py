num = [1, 2, 3, 4, 5]
result1 = []
result2 = []
# [2, 4, 6, 8, 10] 출력
for i in num:
    result1.append(i * 2)
print(result1)
# 홀수인 값들만 2배 연산 후 출력
for i in num:
    if i % 2 == 1:
        result2.append(i * 2)
print(result2)