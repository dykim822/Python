# 주사위를 두번 던져서 합이 6인 경우를 출력하시오
for i in range(1, 7):   # 첫번째 주사위 눈의 범위 1~6
    for j in range(1, 7):   # 두번째 주사위 눈의 범위 1~6
        k = i + j
        if k == 6:
            print(f"{i} + {j} = {k}")