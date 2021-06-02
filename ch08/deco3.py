class MyDeco:
    def __init__(self, fuc):
        print("초기화");
        self.fuc = fuc
    def __call__(self):
        print(f"시작 : {self.fuc.__name__}")
        self.fuc()
        print(f"종료 : {self.fuc.__name__}")
@MyDeco # 메서드명이 객체명이 되고 생성자에 매개변수로 객체이름이 저장
def print_hello():
    print("안녕 컴 동지들")
print_hello()