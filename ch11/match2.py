import re
print("글자를 입력하세요")
num = input()   # 숫자를 문자형태로 받겠다는 의미
match1 = re.match('[0-9]*', num)    # *는 0개 이상
print(match1.group())
match1 = re.match('[0-9]', num)
print(match1)
# print(match1.group()) match되는 것이 하나도 없으면 group 사용 불가
match1 = re.match('[0-9]+', num)     # +는 1개 이상
print(match1)
print(match1.group())