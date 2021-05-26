#     0  1  2
l1 = [1, 2, 3]
#       0       1     2       3
l2 = ['life', 'is', 'too', 'short']
#       -4     -3     -2      -1
l3 = []     # list 생성
l4 = list() # list 생성
print(l1[1])
print(l2[2])
print(l1[1] + l1[2])
print(l2[-1])
l5 = ['life', 'is', 'too', 'short', [1,2,3]]
print(l5[-1])
print(l5[-1][0])        # [1,2,3] 중 1 출력
print(l5[-1][-1])       # [1,2,3] 중 3 출력