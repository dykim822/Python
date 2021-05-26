# 자릿수 합계 ex) 367 => 3+6+7=16
print("정수를 여러 자리 입력해 보세요")
num = int(input())
sum = 0
while num != 0:         # 367 입력했다고 하면
    sum += num % 10     # 0+7   => 7+6  => 13+3 => num=0이므로 stop
    num = num // 10     # 36    => 3    => 0
print(sum)