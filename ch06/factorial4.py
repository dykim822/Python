# factorial
def factorial(num):
    if num > 1:
        print(num, '* ', end='')
        return factorial(num - 1) * num
    else:
        print('1 = ', end='')
        return 1
print(factorial(0))
print(factorial(3))
print(factorial(5))

# num = 5일 떄
# 5 * 4 * 3 * 2 * 1 = result => 120