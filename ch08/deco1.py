class Call1:
    def __call__(self):
        print("누가 날 불렀네")
ob = Call1()
ob() # 객체를 메서드처럼 호출하면 call메서드가 실행된다