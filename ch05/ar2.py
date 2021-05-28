def ar(**args): # ** 키와 값 전달
    for i in args:
        print(i + " : "+ args[i])
ar(a="5월", b="28일", c="금요일", d="날씨 흐림")
# a, b, c, d가 key/ 5월, 28일, 금요일, 날씨 흐림은 값