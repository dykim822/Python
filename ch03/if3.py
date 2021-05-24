# print('요일의 첫글자를 입력하세요')
week = input('요일의 첫글자를 입력하세요 : ')
if week == '월':
    result = "Monday"
# elif => else if
elif week == '화':
    result = "Tuesday"
elif week == '수':
    result = "Wednesday"
elif week == '목':
    result = "Thursday"
elif week == '금':
    result = "Friday"
elif week == '토':
    result = "Saturday"
elif week == '일':
    result = "Sunday"
else:
    result = "다시 입력하세요"
print(result)