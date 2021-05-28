def ar(len, *args):
    for i in range(len):
        print(args[i])
# 가변변수 앞에서 호출할때는 키워드로 하면 안된다!
ar(4, "5월", "28일", "금요일", "날씨 흐림")