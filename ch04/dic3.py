d1 = {} # {} dictionary
print(type(d1))
# key는 중복 불가
d1[5] = 25  # dict이름[키] = 값
d1[2] = 4
d1[3] = 9
print(d1)
print(d1[5])
d1[3] = 12      # key가 같으면 앞 key에 해당하는 값을 덮어쓴다
print('key는 중복 불가!')
print(d1)
print(d1[5])
print(d1.get(3))
print(d1.get(4))    # 존재하지 않는 key를 입력하면 에러가 아니라 None
print(d1.get(4, '목요일')) # 해당하는 값이 없을 때 default값으로 출력 가능
print(d1)

print(5 in d1)      # in; key가 있는지 여부
print(4 in d1)
print(5 not in d1)  # not in; key가 없는지 여부
print(4 not in d1)

print(d1.keys())
print(d1.values())
d1.clear()      # data 전부 삭제
print(d1)