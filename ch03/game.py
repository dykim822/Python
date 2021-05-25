import random
cnt = 0
# 1부터 100사이의 정수가 랜덤하게 발생
ran = random.randint(1, 100)
while True:
    print("1부터 100사이의 정수를 입력하세요")
    num = int(input())
    cnt += 1
    if ran == num:
        break
    elif num > ran:
        print("작은 수를 입력하세요")
    else:
        print("큰 수를 입력하세요")
print(f"{cnt}번만에 정답 {ran}을 맞췄습니다")