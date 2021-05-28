input1 = input("첫 번째 숫자를 입력하세요 : ")
input2 = input("두 번째 숫자를 입력하세요 : ")
# 입력된 값은 문자로 인식한다
total = input1 + input2
print("두수의 합은 %s 입니다" % total)
# 정수로 형변환
total = int(input1) + int(input2)
print("두수의 합은 %s 입니다" % total)