class User:
    def __init__(self, name, email, password):
        self.name = name; self.email = email; self.password = password
    def introduce(self):
        print(f"이름 : {self.name}, 이메일 : {self.email}")
    def introduce_twice(self):
        self.introduce()
        self.introduce()

user1 = User("철수", "chul@korea.kr", 11)
user2 = User("영희", "young@korea.kr", 22)
user1.introduce(); user1.introduce_twice()
print("==================================")
User.introduce(user2); User.introduce_twice(user2)