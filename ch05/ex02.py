def average_numbers(*args): # 단어가 여러개 들어올 수 있다는 의미
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)
print("평균 :", average_numbers(10, 20, 30))
print("평균 :", average_numbers(10, 12, 16))
print("평균 :", average_numbers(1, 2))
print("평균 :", average_numbers(1, 2, 3, 4, 5))