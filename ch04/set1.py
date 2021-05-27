# list 생성 방법 li = [], li = list()
s1 = set()
# s1 = {} 안됨, dictionary도 {}사용
print(s1)
s2 = {1, 2, 3}
print(s2)
s3 = set((1, 2, 3, 2))
print(s3)   # set; 중복되는 값은 출력하지 않는다
s4 = set('hello world')
print(s4)   # 각각의 단어를 값으로 생각하고 처리하는데 중복된 단어는 한번만 출력
s5 = set([1, 2, 3, 2])
print(s5)
