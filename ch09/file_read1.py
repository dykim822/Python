file = open('test.txt', 'r', encoding='utf-8')
for i in file:
    # print(i) 그냥 쓰면 한줄씩 띄어서 출력
    print(i, end='')
file.close()
print('=====================')
file = open('test.txt', 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()
print('=====================')
file = open('test.txt', 'r', encoding='utf-8')
lines = file.readlines()    # list형식으로 변경하여 읽기
print(lines)
file.close()