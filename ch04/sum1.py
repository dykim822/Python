sum = 0
# 1000번 실행
for i in range(0, 1000):
    sum += 1
print("합계 : ", sum)
# sum을 실수로 정의하고 실수를 더하게 되면 부동소수 0.1로 계산하기 때문에 오차가 발생한다
sum = 0.0
for i in range(0, 1000):
    sum += 0.1  # 부동소수 0.1로 정확한 0.1이 아니다!
print("합계 : ", sum)