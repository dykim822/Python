# while-for문을 혼합한 구구단 입력
while True:
    print("구구단 단수를 입력하세요")
    num = int(input())
    if num >= 2 and num < 10:
        print(f"구구단 {num}단")
        for i in range(1, 10):
            print(f"{num} * {i} = {num * i}")
    elif num == 0:
        break
    else:
        print("다시 입력해주세요")
print("프로그램 종료")