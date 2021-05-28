# nationality 매개변수에 값이 없으면 default값으로 한국을 이용한다
def myself(name, age, nationality="한국"):
    print("이름 :", name)
    print("나이 :", age)
    print("국적 :", nationality)
    print("==================")
myself("철수", 25, "미국")
myself("영희", 47)