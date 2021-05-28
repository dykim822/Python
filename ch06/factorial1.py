# factorial
def factorial(num):
    result = 1
    for i in range(1, num + 1):     # 1 <= i < num+1 => num개
        result = result * i
    return result

print(factorial(0))
print(factorial(3))
print(factorial(5))