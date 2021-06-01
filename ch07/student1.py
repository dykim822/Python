class Student:
    def start(self):
        print("안녕하세요")
    def printName(self, name):
        print(f"이름은 {name}입니다")

if __name__ == "__main__":
    stu = Student()
    Student.start(stu)
    stu.printName("철수")