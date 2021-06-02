class Person:
    def speak(self):
        print("떠든다")
    def move(self):
        print("두발로 움직인다")
class Fish:
    def move(self):
        print("지느로미로 헤엄친다")
class MurMaid(Fish, Person):
    pass
mm = MurMaid()
mm.speak()
mm.move()