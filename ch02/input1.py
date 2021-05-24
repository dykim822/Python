print("숫자를 입력하세요")
a = input()     # input으로 받는 데이터는 문자열로 취급
print("숫자를 입력하세요")
b = input()
# print(a * b) 그냥 출력하면 에러! 형변환 필요!
print(int(a) * int(b))

# Java에서 String.format과 유사
print("{} * {} = {}".format(a, b, int(a)*int(b)))