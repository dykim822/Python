def print_something(a):
    print(a)
def plus(x, y):
    return x + y
print_something(120)
p = print_something     # 함수를 변수에 저장
p(12)
p(45)
p1 = [print_something, plus]    # 함수를 list에 저장
p1[0](12)
print(p1[1](12, 56))