import pickle
class Dto:
    def setNum(self, num):
        self.num = num
    def setName(self, name):
        self.name = name
    def getNum(self, num):
        return self.num
    def getName(self, name):
        return self.name
    def toString(self):
        return "{번호 : "+ str(self.num) +", 이름 : "+ self.name+"}"
data1 = Dto(); data1.setNum(1); data1.setName("Kim")
data2 = Dto(); data2.setNum(2); data2.setName("Park")
li = [data1, data2]
with open('test3.txt', 'wb') as f:
    pickle.dump(li, f)
with open('test3.txt', 'rb') as f:
    result = pickle.load(f)
    for i in result:
        print(i.toString())