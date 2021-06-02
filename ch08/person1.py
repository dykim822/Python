# 객체지향언어의 특정 => 다형성
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def prn(self):
        print("===================")
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
class Student(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby
    def prn(self):
        super().prn()
        print(f"취미 : {self.hobby}")
class Teacher(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    def prn(self):
        super().prn()
        print(f"과목 : {self.major}")
class Staff(Person):
    def __init__(self, name, age, part):
        super().__init__(name, age)
        self.part = part
    def prn(self):
        super().prn()
        print(f"담당 : {self.part}")
st1 = Student("철수", 25, "코딩"); st2 = Student("영희", 22, "노래")
th1 = Teacher("민수", 36, "수학"); th2 = Teacher("윤희", 46, "미술")
sf1 = Staff("경민", 29, "청소"); sf2 = Staff("민경", 21, "발권")
x = [st1, st2, th1, th2, sf1, sf2]
for i in x:
    i.prn()