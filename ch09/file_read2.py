with open('voca.txt', 'r', encoding='utf-8') as file:
    for i in file:
        data = i.strip().split(': ')
        eng = data[0]
        kor = data[1]
        print(f"{kor}에 해당되는 영어는?")
        eng_ans = input()
        if eng == eng_ans:
            print('정답!')
        else:
            print(f'오답! 정답은 {eng}입니다')
    print('프로그램 종료')