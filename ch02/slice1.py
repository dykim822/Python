#    0123 4 56 7 890 1 234567 8 901 2 3456 7 890123
a = "Life is too short, You need Python"
print(a[3])
print(a[10])    # 인덱스 10번째 문자
print(a[-3])    # 끝에서 3번째 문자
print(a[0:4])   # 인덱스 0부터 4앞까지
print(a[5:7])
print(a[:])     # 처음부터 끝까지 출력
print(a[10:])   # 인덱스 10부터 끝까지
print(a[10:-2]) # 인덱스 10부터 끝에서 2번째 바로 앞까지
print(a[:10:2]) # 처음부터 10전까지 인덱스 0,2,4,6,8 출력