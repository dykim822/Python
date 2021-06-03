file = open('test.txt', 'w', encoding='utf-8')
file.write("Hello\n")
lines = ['안녕하세요', '반갑습니다', '파이썬입니다\n']
# 한줄 띄고 안녕하세요 출력, 한줄 띄고 반갑습니다, 한줄 띄고 파이썬입니다
file.write('\n'.join(lines))
line2 = ['2021년\n', '6월\n', '3일\n']
file.write(''.join(line2))
file.close()