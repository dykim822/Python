# factorial
def factorial(num):
    result = 1
    # 1*2*3 => 3 * 2 * 1 = 6
    # 1*2*3*4*5 => 5 * 4 * 3 * 2 * 1 = 120
    for i in range(num, 1, -1):     # num부터 1까지 1씩 빼서 대입
        if num == 0:
            return 1
        print(i, '* ', end='')
        result *= i
    print('1 = ', end='')
    return result

print(factorial(0))
print(factorial(3))
print(factorial(5))