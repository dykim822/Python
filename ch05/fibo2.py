def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
print(fibo(7))
# 1 1 2 3 5 8 13 21 34 55