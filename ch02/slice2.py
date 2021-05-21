#    012345
a = 'Pithon'
# i를 y로 변경
# 문자열은 일부만 변경이 불가
# 문자열을 추가하거나 삭제할 때는 슬라이싱, 연결을 사용해야 한다
b = a[:1]+'y'+a[2:]
print(b)

#       012345678901234567
str1 = "Hardware and Shell"
print(str1[:8]+' Kernel'+str1[8:])
print(str1[:8]+str1[12:])