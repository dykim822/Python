l1 = [2, 7, 3, 6]
# l1.sort(): list 데이터가 변경
l2 = sorted(l1)     # 원본 데이터는 변경하지 않고 정렬된 결과를 l2에 저장
print("원본", l1)
print("오름차순", l2)
l3 = sorted(l1, reverse=True)   # 원본 데이터는 변경x
print("원본", l1)
print("내림차순", l3)
# l1.reverse(): 원본 데이터 순서를 반대로 한다-> 데이터가 바뀐다
l1.sort(reverse=True)   # 원본 데이터를 내림차순으로 변경-> 데이터가 바뀐다
print("원본 변경", l1)