import sys
print('정수를 입력하세요')
num = int(input())
# python은 0또는 데이터가 없으면 false
if num != 0:
    print('반갑습니다')
else:
    print('누구세요?')
    # sys.exit() 프로그램 정상 종료 => 프로그램 종료가 출력되지 않는다
    sys.exit(0)
print('프로그램 종료')