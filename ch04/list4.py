a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 = [4, 5, 6]
a3 = "123"
print(a1 + a2)
print((a1 * 3))     # list 반복
print(len(a1))      # 인덱스 갯수(길이)
print(str(a1[1]) + 'hi')    # 숫자+문자를 위해서는 str 형변환 필요
a1[1] = 7   # 데이터 변경 가능
print(a1)
# a3[1] = 7 이런 식으로 문자열은 변경할 수 없다
del a1[3:]      # a1의 인덱스 3부터 데이터를 삭제
print(a1)
a2.append(7)    # append; 맨뒤에 추가
print(a2)
a2.append([8, 9])
print(a2)