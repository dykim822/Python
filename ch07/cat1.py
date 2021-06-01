class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("야옹")
    def drink(self, food):
        print(f"{self.name}이 {food}를 먹는다")

if __name__ == "__main__":
    cat1 = Cat("냥이");   cat2 = Cat("고양")
    cat1.speak();   cat1.drink("우유")
    Cat.speak(cat2); Cat.drink(cat2, "막걸리")