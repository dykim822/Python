li = [1, 6, 3]
# {1:3d} 1은 format 뒤에 있는 인덱스번호, 3d는 정수3자리 확보
print("최대값:{0:3d}\t최소값:{1:3d}".format(max(li), min(li)))
#       0123456789012345
str1 = "c:/data/data.txt"
# test있는지 확인
print(str1.find("test"))    # test가 있으면 test가 시작하는 인덱스 번호 출력 없으면 -1
print(str1.find('.'))
print(str1.rfind('.'))
print(str1.find('/'))
print(str1.rfind('/'))      # 뒤부터 찾아서 인덱스 번호 출력
n = str1.find('.')
print('확장자명 :', str1[n+1:])
m = str1.rfind('/')
print("패키지명 :", str1[:m])
# str1을 .기준으로 배열로 생성
list = str1.split('.')
print(list)
print('총 글자 수 :', len(str1))    # index 0~15
print('배열 갯수 :', len(list))
print('확장자명 :', list[len(list) - 1])    # list[1] 출력이므로 text출력!
# data를 python으로 변경
print(str1.replace('data', 'python'))