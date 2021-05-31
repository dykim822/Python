from functools import reduce
# 보통 머신러닝, 딥러닝에서 주로 내부 reduce를 이용해 연산, 처리
print(reduce(lambda x, y:x+y, [47, 11, 42, 13]))
x = [47, 11, 42, 102, 13]
f = lambda a, b: a if(a>b) else b
print(reduce(f, x))