a = [1, 2, 3]
a.insert(0, 4)  # 인덱스 0번째에 4를 대입
print(a)
a.insert(2, 2)
a.insert(2, 5)
print(a)
a.remove(2) # 첫번째 2인 값 1개을 삭제
# del은 해당 인덱스 값을 삭제/ remove는 해당 값을 삭제
print(a)
print(a.pop())  # 마지막 데이터를 끄집어서 출력하고 삭제
print(a)
print(a.pop(0)) # 인덱스 0번째 데이터를 출력하고 삭제
print(a)