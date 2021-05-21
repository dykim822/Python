# 순서에 맞게 각각 대입
a1, b1 = 3, 5
# java에서 값 교환 시
imsi = a1
a1 = b1
b1 = imsi
print('a1 = ',a1)
print('b1 = ',b1)
# python에서는 서로 swap이 가능
a1, b1 = 3, 5
a1, b1 = b1, a1
print('a1 = ',a1)
print('b1 = ',b1)