class User:
    # __init__ 자바의 생성자와 유사
    def __init__(self, name, age, email):
        self.name = name;   self.age = age;   self.email = email;
    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 이메일 : {self.email}")

user1 = User("영희", 28, "young@korea.kr")
user2 = User("철수", 50, "chul@korea.kr")
user3 = User("길동", 34, "gil@korea.kr")
user1.introduce();  user2.introduce(); user3.introduce()