#    0123456789012
a = '20210521Rainy'
# 연월일만 출력
date = a[:8]
print('날짜 : ', date)
# 날씨만 출력
weather = a[8:]
print('날씨 : ', weather)
# 월일만 출력
md = a[4:8]
print('월일 : ', md)
month = md[1]
day = md[2:]
print('월일 : ', month, end='월'+day+'일')