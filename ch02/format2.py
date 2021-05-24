print("나는 사과를 {}개 먹는다".format(3))
number = 3
print("나는 사과를 {}개 먹는다".format(number))
day = "3일"
print("나는 사과를 {}에 {}개 먹는다".format(day, number))
print("나는 사과를 {0}에 {1}개 먹는다".format(day, number))
# 숫자는 뒤에 있는 값의 인덱스 번호
print("나는 사과를 {1}에 {0}개 먹는다".format(day, number))
print("나는 사과를 {day}에 {number}개 먹는다".format(day='3일', number=3))