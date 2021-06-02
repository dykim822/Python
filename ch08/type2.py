# type 클래스 생성기능도 있다
class A:
    attr = "정적 클래스"
ob1 = A()
print(ob1.attr)
#       클래스명 생성         속성
# 1회용으로 사용
ob2 = type("B", (), {"attr": "동적 클래스"})
print(ob2.attr)