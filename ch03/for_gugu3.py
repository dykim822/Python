# for문, range를 활용한 2~9단까지 구구단
for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j} * {i} = {j * i}", end="\t")
    print()