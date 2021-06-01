class Student:
    schoolName = "중앙"   # 클래스 변수, java에서 static, 전역변수
    def __init__(self, name, age, hobby):
        self.name = name;   self.age = age;   self.hobby = hobby;   # instance 변수, 지역변수
    def print1(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 취미 : {self.hobby}")
st1 = Student("영희", 34, "게임")
st2 = Student("철수", 52, "포기")
st1.print1();   Student.print1(st2)
print(Student.schoolName)
print(st1.schoolName, st2.schoolName)