import re
match1 = re.match('[0-9]', ' 1234')  # match 첫번째 데이터를 먼저 확인하고 맞는지 체크
print(match1)
match1 = re.match('\s[0-9]', ' 1234')    # \s 첫글자가 공란
print(match1)
match1 = re.search('[0-9]', ' 1234') # 전체 데이터에서 검색
print(match1)