# Generator
g1 = [n*n for n in range(21)]
print(g1)
# list와 비슷하지만 소괄호로 처리
g2 = (n*n for n in range(21))
l1 = list(g2)
print(l1)

g3 = (n*n for n in range(21))
for i in range(10):
    val = next(g3)
    print(val)
print("===============")
# generator로 생성하면 yield처럼 사용된 것을 제외하고 다음 것이 반영
for i in g3:
    print(i)