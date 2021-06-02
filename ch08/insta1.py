from abc import ABCMeta, abstractmethod
class Car(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        pass
class Ambulance(Car):
    def drive(self):
        print("환자를 싣고 달린다")
    def move(self):
        print("경적을 울리면서 이동한다")
class Taxi(Car):
    def drive(self):
        print("총알처럼 달린다")
cars = [Ambulance(), Taxi()]
for car in cars:
    car.drive()
    if isinstance(car, Ambulance):  # java의 car instance of Ambulance와 같은 역할
        car.move()  # Ambulance인 경우에만 실행