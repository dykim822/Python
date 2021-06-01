class Student:      # __ 의미: 자신이 private라는 뜻
    def __init__(self, name="무명"):
        self.name = name
    def setName(self, name):
        print("setter method 호출")
        self.__name = name
    def getName(self):
        print("getter mehtod 호출")
        return self.__name
    def setAge(self, age):
        print("setter method 호출")
        if age < 0:
            print("잘못된 나이입니다")
            self.__age = 0
        else:
            self.__age = age
    def getAge(self):
        print("getter mehtod 호출")
        return self.__age
    # 직접 멤버변수로 데이터를 저장하거나 불러와도 실제로 실행은 메서드가 실행
    name = property(fset=setName, fget=getName)
    age = property(getAge, setAge)  # get을 먼저 사용하면 fset,초 fget 생략 가능
st1 = Student("영희")
print(st1.name)
st1.name = "철수"
st1.age = -10
print(f"이름 : {st1.name}, 나이 : {st1.age}")