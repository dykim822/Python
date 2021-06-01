class User:
    pass

user1 = User()
user2 = User()
user3 = User()
print(type(user1))
print(type(user2))
print(user1 == user2)   # 각각의 인스턴스이므로 당연히 다르다
user1.name = "영희";  user1.age = 20; user1.email = "young@korea.kr"
user2.name = "철수";  user2.age = 45; user2.email = "chul@korea.kr"
user3.name = "길동";  user3.age = 25; user3.email = "gil@korea.kr"
print(user1.name, user1.age, user1.email)
print(user2.name, user2.age, user2.email)
print(user3.name, user3.age, user3.email)
# print(user1.address)    # 생성, 정의하지 않은 속성 출력 시 에러 발생