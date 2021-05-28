def f(a):
    a[0] = 100
    print("지역변수 :", a)
# list, tuple, dic, 객체(변수가 여러 개 값을 가진 경우)인 경우에는 주소를 전달
a = [1, 2, 3]
f(a)
print("전역변수 :", a)