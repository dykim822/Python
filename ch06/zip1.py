a1 = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
a2 = [95, 90, 90, 90, 95, 100, 90, 80, 95, 90]
# 2개의 리스트를 합쳐서 각 리스트 원소의 쌍으로 갖는 리스트 생성
a = list(zip(a1, a2))
print(a)
s = []
for i, j in a:
    s.append(i+j)
print(s)
print('sum[a1] =', sum(a1))
print('sum[a2] =', sum(a2))
print('sum[s] =', sum(s))