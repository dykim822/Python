class User:
    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 이메일 : {self.email}")

user1 = User()
user2 = User()
user3 = User()

user1.name = "영희";  user1.age = 20; user1.email = "young@korea.kr"
user2.name = "철수";  user2.age = 45; user2.email = "chul@korea.kr"
user3.name = "길동";  user3.age = 25; user3.email = "gil@korea.kr"

User.introduce(user1);  User.introduce(user2);  User.introduce(user3)
print("================================================")
user1.introduce(); user2.introduce(); user3.introduce()