# 자릿수 합계 ex) 367 => 3+6+7=16
print("정수를 여러 자리 입력해 보세요")
num = input()               # 처음에 문자로 처리
sum = 0
for i in range(len(num)):   # 각각의 문자를 숫자로 바꿔서 연산
    sum += int(num[i])
print(sum)