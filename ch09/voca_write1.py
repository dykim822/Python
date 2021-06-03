file = open('voca.txt', 'w', encoding='utf-8')
while True:
    print("영어 ")
    eng = input()
    if eng == 'q':
        break
    print("한글 ")
    kor = input()
    file.write(f"{eng}: {kor}\n")
print("단어장 완성")
file.close()