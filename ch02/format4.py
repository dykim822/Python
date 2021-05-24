# { test } 형식으로 출력 format과 같이 사용할 시 {{}}로 처리한다ㅉ
print("{{중요한}} 사건이야 이 {}에서는...".format("바닥"))
name = "홍길동"
age = 25
# 파이썬 3.6부터 지원하는 format
print(f"이름은 {name}이고 나이는 {age}")
print(f"이름은 {name}이고 나이는 {age}이지만 내년에는 {age+1}살 입니다")
# Java에서 map과 비슷한 것이 python에서는 diction이라 부른다
d = {'name':'홍길동', 'age':30}
print(f"이름은 {d['name']}이고 나이는 {d['age']}입니다")