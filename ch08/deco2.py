class MyDeco:
    def __init__(self, fuc):
        print("초기화");
        self.fuc = fuc
    def __call__(self):
        print(f"시작 : {self.fuc.__name__}")
        self.fuc()
        print(f"종료 : {self.fuc.__name__}")
def print_hello():
    print("안녕 컴 동지들")
md = MyDeco(print_hello)
md()