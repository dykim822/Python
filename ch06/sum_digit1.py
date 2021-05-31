# 문자로 변경해서 구하는 프로그램
def sum_digits(n):
    if n < 10:
        return n
    else:
        str_n = str(n)
    return int(str_n[0]) + sum_digits(int(str_n[1:]))
# 2 + sum_digits(2541) => 2 + 2 + sum_digits(541) => ... => 2 + 2 + 5 + 4 + sum_digits(1) => 2+2+5+4+1
# 문자로 변경하지 않고 구하는 프로그램
def sum_digits2(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits2(n // 10)

def sum_digits3(n):
    sum = 0
    while n != 0:
        sum += n % 10   # sum = 0 + 22541 % 10 => sum = 1
        n = n // 10     # n = 22541 // 10 => n = 2254
    return sum
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
print("=================")
print(sum_digits2(22541))
print(sum_digits2(92130))
print(sum_digits2(12634))
print(sum_digits2(704))
print(sum_digits2(3755))
print("=================")
print(sum_digits3(22541))
print(sum_digits3(92130))
print(sum_digits3(12634))
print(sum_digits3(704))
print(sum_digits3(3755))