import re
match1 = re.match('[0-9]', '1234')
print(match1.group())
match1 = re.match('[0-9]', 'abcd')
print(match1)
# print(match1.group()) match되는 것이 하나도 없으면 group 사용 불가
match1 = re.match('[0-9]+', '1234')     # +는 1개 이상
print(match1)
print(match1.group())