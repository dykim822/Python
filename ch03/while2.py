num = 1
while num != 0:
    print('구구단 단수를 선택하세요')
    num = int(input())
    if num >= 2 and num <= 9:
        i = 1
        while i <= 9:
            print(f"{num} * {i} = {num * i}")
            i += 1
    else:
        print("올바른 숫자를 입력해주세요")
print('프로그램 종료')