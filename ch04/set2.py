a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b))   # union: 합집합 A U B
print(a.intersection(b))    # intersection: 교집합 A n B
print(a.difference(b))      # difference: 차집합 A-B
print(b.difference(a))      # B - A
print(a.symmetric_difference(b))    # (A U B) - (A n B)
print(5 in a)   # 포함 여부 True/False
print(7 in a)
print(5 not in a)
print(7 not in a)