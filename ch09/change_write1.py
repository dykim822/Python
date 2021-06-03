with open('test2.txt', 'w', encoding='utf-8') as f1:
    # print시 console창에 출력되지 않고 연결된 file(f1)에 저장
    print('2021년', file=f1)
    print('6월', file=f1)
with open('test2.txt', 'r', encoding='utf-8') as f1:
    print(f1.read())