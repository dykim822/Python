l1 = list(range(10)) # 0부터 4전까지(0~3) list 생성
print(l1)
del l1[::2] # 0, 2, 4 ... 인덱스 데이터 삭제
print(l1)
l1[1:1] = [2]   # 인덱스 1번째에 2를 추가
print(l1)
l1[0:0] = [0]   # 인덱스 0번째에 0을 추가
print(l1)
for i in l1:
    print(i)