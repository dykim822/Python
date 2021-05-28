def f():
    global x    # 지역변수를 전역변수로 사용하겠다는 의미
    x = 10
    print("함수 내부 :", x)

x = 7
f()
print("함수 외부 :", x)