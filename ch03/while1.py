sum = 0
cnt = 1
while cnt <= 100:
    sum += cnt
    cnt += 1
else:   # python에서는 else를 사용할 수 있다, 생략도 가능하다!
    print(f'현재 cnt는 {cnt}입니다')
print(f'합계 : {sum}')