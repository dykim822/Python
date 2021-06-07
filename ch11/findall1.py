import re
match1 = re.findall('[0-9]', ' 1234')  # findall 모든 문자 확인
print(match1)
match1 = re.findall('\s[0-9]', ' 1234')    # \s 첫글자가 공란
print(match1)
match1 = re.search('[0-9]', ' 1234') # match는 첫번째 글자 확인
print(match1)