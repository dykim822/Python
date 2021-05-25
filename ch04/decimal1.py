from decimal import Decimal
sum = Decimal(0.0)  # 정확한 0.0이라는 뜻
delta = Decimal("0.1")  # 정확한 0.1/ 큰 따옴표도 상관없음
for i in range(0, 1000):
    sum += delta
print("합계 :", sum)