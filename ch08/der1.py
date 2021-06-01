class Base:
    def base_method(self):
        print("난 부모메서드")
class Derived(Base):    # 상속 표시를 (부모클래스)
    def der_method(self):
        print("난 자식 메서드")
b = Base()
b.base_method()
d = Derived()   # 부모의 메서드와 멤버면수를 자기것처럼 사용 가능
d.base_method()
d.der_method()