# factorial
def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1
print(factorial(0))
print(factorial(3))
print(factorial(5))