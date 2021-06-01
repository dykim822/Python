class P1:
    def __init__(self, name):
        print("P1.__init__()")
        self.message = "안녕"
        print(name)
    def pr(self):
        print("6월1일")
# 자바에서는 자식을 생성하면 부모의 생성자가 먼저 실행하고 자식 생성자가 실행
# python은 부모의 생성자를 실행시키지 않는다
class C1(P1):
    def __init__(self):
        print("C1.__init__()")
        # 부모의 생성자를 호출하여 실행시켜야 한다
        # java에서는 부모 호출하는 메서드가 첫번째 줄에 있지만 python은 상관없다
        super().__init__("영희")
        print("메세지 : "+self.message)
ob = C1()
ob.pr()