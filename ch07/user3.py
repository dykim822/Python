class User:
    def initialize(self, name, age, email):
        self.name = name; self.age = age; self.email = email
    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 이메일 : {self.email}")

user1 = User(); user2 = User(); user3 = User()
user1.initialize("영희", 28, "young@korea.kr")
user2.initialize("철수", 50, "chul@korea.kr")
user3.initialize("길동", 34, "gil@korea.kr")
user1.introduce();  user2.introduce(); user3.introduce()