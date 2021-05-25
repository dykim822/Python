print("구구단 단수를 입력하세요")
num = int(input())
if num >= 2 and num < 10:
    print(f"구구단 {num}단")
    for i in range(1, 10):
        print(f"{num} * {i} = {num * i}")
else:
    print("다시 입력해주세요")