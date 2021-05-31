# i는 index, e에는 값
for i, e in enumerate(["a", "b", "c"]):
    print(i, ":", e)

# eval : 문자열에 포함된 식을 실행
a1 = '1 + 2'
print(a1)
print(eval(a1))