numbers = []
# 1부터 10까지 채우기
numbers[0:0] = range(1, 11)
print(numbers)
# 홀수 삭제
del numbers[::2]    # 인덱스 0, 2, 4, ... 삭제
print(numbers)
# 인덱스 0에 20 추가
numbers.insert(0, 20)
print(numbers)
# 정렬해서 출력
numbers.sort()
print(numbers)
numbers.reverse()   # 이렇게 내림차순 구현도 가능
print(numbers)