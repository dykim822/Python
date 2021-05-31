import time
print(time.time())
print(time.localtime(time.time()))
# 현재 날짜, 시간
print(time.asctime(time.localtime(time.time())))
print(time.ctime()) # current time
# string format time
print(time.strftime('%Y/%m/%d(%A) %H:%M:%S', time.localtime(time.time())))