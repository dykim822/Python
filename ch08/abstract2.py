from abc import *
class Animal (metaclass=ABCMeta):
    def eat(self):
        print("음식을 먹는다")
    @abstractmethod
    def move(self):
        pass
class Bird(Animal):
    def move(self):
        print("하늘을 난다")
class Fish(Animal):
    def move(self):
        print("헤엄 친다")
class Person(Animal):
    def move(self):
        print("두 발로 걷는다")
an = [Bird(), Fish(), Person()]
for a in an:
    a.eat()
    a.move()