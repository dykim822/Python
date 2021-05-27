keys = ['one', 'two', 'three', 'four']
values = (1, 2, 3)
d1 = dict(zip(keys, values))    # dict; 서로 일대일대응을 시켜준다
print(d1)
for i in d1:
    print(i, ":", d1[i])