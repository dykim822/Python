# 1 ~ 1000 3의 배수 합
sum = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        sum += i
        # print(i)
    i += 1
print("1부터 1000까지 합 : ", sum)