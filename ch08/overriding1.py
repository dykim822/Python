class A:
    def m1(self):
        print("2021년 6월 2일")
class B(A):
    def m1(self):
        print("수요일")
class C(A):
    def m1(self):
        print("벌써")
a = A(); b = B(); c = C()
a.m1(); b.m1(); c.m1()
# 부모와 자식이 같은 메서드명이면 자식 메서드를 실행