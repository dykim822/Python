file = open('chicken.txt', 'r', encoding='utf-8')
print(type(file))
# 'r'읽는다는 의미, 한글 읽기 위해 utf-8 인코딩
for i in file:
    print(i, end="")
file.close()