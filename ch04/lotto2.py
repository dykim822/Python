from random import randint
lotto = set()       # 중복 안되게 하기 위해 set
while len(lotto) < 6:
    ran = randint(1, 45)    # 1 ~ 45 사이의 정수 random 생성(1, 45도 포함)
    lotto.add(ran)
print("로또번호 : ", sorted(lotto))