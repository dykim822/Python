a = [1, 2, 3, 1]
print(a.count(1))
a.extend([4, 5])    # 현재의 list에 [4,5] list를 추가
# append와의 차이점 구별!
print(a)
print(a + [8, 2])   # +연산으로도 추가 가능(extend와 같은 기능)