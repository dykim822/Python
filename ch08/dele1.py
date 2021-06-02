class Delegation:
    def __init__(self, li):
        self.li = li
    def __getattr__(self, name):    # 존재하지 않는 메서드를 요청하면 대신 실행/ name은 요청한 메서드명
        print(f"위임 : {name}", end="")
        return getattr(self.li, name)   # self.li의 데이터에 name에 해당하는 메서드 실행
ob = Delegation([1, 3, 5, 3, 9, 1])
print(ob.pop()) # pop 메서드; 마지막 값 삭제
print(ob.count(3))