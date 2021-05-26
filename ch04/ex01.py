print("문자를 입력하세요")
str1 = input()
print(str1[::-1])
# 반복문으로 거꾸로 출력하기
l = len(str1) -1    # 인덱스는 0부터 시작
while l >= 0:
    print(str1[l], end="")
    l = l - 1
print()
# 마지막 인덱스, -1 바로 앞=> 인덱스 0까지, 인덱스를 1씩 감소
for i in range(len(str1) -1, -1, -1):
    print(str1[l], end="")
    l = l -1