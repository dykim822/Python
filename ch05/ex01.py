def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
print(is_odd(7))
print(is_odd(6))

# 아래와 같이 더 간단히 할 수 있다
def is_odd2(number):
    return number % 2 ==1
print(is_odd2(7))
print(is_odd2(6))