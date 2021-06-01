class Student:
    schoolName = "중앙"
    def setName(self, name):
        self.name = name;
    def getName(self):
        return self.name
    def setAge(self, age):
        if age < 0:
            print("잘못된 나이입니다")
        else:
            self.age = age
    def getAge(self):
        if self.age < 0:
            print("잘못된 나이입니다")
        else:
            return self.age

st1 = Student(); st1.setName("철수"); st1.setAge(53)
print(f"이름 : {st1.getName()}, 나이 : {st1.getAge()}")
st2 = Student(); st2.name = "영희"; st2.age = 23
print(f"이름 : {st2.name}, 나이 : {st2.age}")
st3 = Student(); st3.name = "길동"; st3.age = 10
print(f"이름 : {st3.name}, 나이 : {st3.age}")
# 멤버 변수에 직접 접근하지 않고 메서드 통해서 접근하면 잘못된 정보의 저장이나 호출을 방지할 수 있다
st4 = Student(); st4.setName("민수"); st4.setAge(-20)
print(f"이름 : {st4.getName()}, 나이 : {st4.getAge}")
