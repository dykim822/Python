# 가변 매개변수 뒤에 정의된 일반변수를 호출할 때는 keyword형식으로 해야 한다
def ar(*args, len):
    for i in range(len):
        print(args[i])
ar("5월", "28일", "금요일", "날씨 흐림", len=4)