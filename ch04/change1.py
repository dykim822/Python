print('잔액을 입력하세요')
money = int(input())
unit = [50000, 10000, 5000, 1000]
for i in unit:
    print(f"{i}원짜리 지폐 : {money//i}장")
    money = money % i