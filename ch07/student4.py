from time import ctime
class Student:
    schoolName = "중앙"
    # 생성자
    def __init__(self, name="무명"):
        print(f"{ctime()}에 객체가 생성되었습니다")
        self.name = name
    # 소멸자
    def __del__(self):
        print(f"{ctime()}에 객체가 소멸되었습니다")
st1 = Student("철수"); st2 = Student("영희")
print(f"이름 : {st1.name}")
del st1 # 중간에 강제로 객체 소멸
print(f"이름 : {st2.name}")
# 작업이 종료되면 소멸자를 불러서 메모리에서 자동 제거쇙