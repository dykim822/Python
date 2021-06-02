from abc import *
class Employ(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def cal_sal(self):
        pass
    def bonus(self):
        self.sal = self.cal_sal()
        self.bonus = self.sal * 0.1
    def prn(self):
        print("================")
        print(f"이름 : {self.name}")
        print(f"급여 : {self.sal:.2f}")
        print(f"보너스 : {self.bonus:.2f}")
class SalaryMan(Employ):
    def __init__(self, name, annual):
        super().__init__(name)
        self.annual = annual
    def cal_sal(self):
        return self.annual / 12
    def prn(self):
        super().prn()
        print(f"연봉 : {self.annual}")
class HourlyMan(Employ):
    def __init__(self, name, work_hour, money_per_hour):
        super().__init__(name)
        self.work_hour = work_hour
        self.money_per_hour = money_per_hour
    def cal_sal(self):
        return self.money_per_hour * self.work_hour
    def prn(self):
        super().prn()
        print(f"시간 단가 : {self.money_per_hour}")
        print(f"근무시간 : {self.work_hour}")
s1 = SalaryMan("김희철", 500000)
s2 = SalaryMan("신동엽", 400000)
s3 = SalaryMan("이영자", 380000)
h1 = HourlyMan("철수", 10, 9000)
h2 = HourlyMan("영희", 20, 10000)
h3 = HourlyMan("민수", 15, 12000)
emps = [s1, s2, s3, h1, h2, h3]
for emp in emps:
    emp.bonus()
    emp.prn()