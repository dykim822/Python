class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}이 야옹하고 웁니다")
    def drink(self):
        print(f"{self.name}이 우유를 마십니다")
        print(f"{self.name}이 낮잠을 잡니다")

romeo = Cat("로미오")
juliet = Cat("줄리엣")
romeo.speak();  romeo.drink()
juliet.speak(); juliet.drink()