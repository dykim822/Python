from random import randint
number = []
print('몇 개를 지정된 번호로 하시겠습니까?')
num = int(input())
while len(number) < num:                # 데이터 수동 입력
    print('어떤 수를 선택하시겠습니까?')    #
    num1 = int(input())                 #
    if num1 not in number:              #
        number.append(num1)             #
while len(number) < 6:
    ran = randint(1, 45)   # 1~45사이 정수
    if ran not in number:   # 발생한 숫자가 number에 없으면
        number.append(ran)
print(sorted(number))