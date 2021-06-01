class Student:
    @classmethod
    def cmethod(cls):
        print("클래스 메서드야")
        print(cls)
    @staticmethod
    def smethod():
        print("난 정적 메서드야")
# 두개 모두 객체를 생성하지 않고 바로 사용 가능
Student.cmethod()
Student.smethod()