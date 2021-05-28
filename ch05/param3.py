# **변수명 ; 나머지를 dict 형태로 데이터를 저장
def f(width, height, **kw):
    print(width)
    print(height)
    print(kw)
f(width=10, height=20, depth=30, dimension=40, a=30)