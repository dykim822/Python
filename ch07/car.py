class Car:
    def __init__(self): # 생성자 역할
        # self; java에서 this와 유사한 역할
        self.color = 0xff0000       # 속성, 멤버변수
        self.wheel_size = 16        # 속성, 멤버변수
        self.displacement = 2000    # 속성, 멤버변수
    def forward(self):              # 메서드
        pass
    def backward(self):
        pass

my_car = Car()      # 객체 생성이 간단하다!
print(my_car.wheel_size)