# split은 뒤에 delimiter기준으로 list형식으로 변경
print("1.2.3.4.5.6".split('.'))
print("1. 2. 3. 4. 5. 6".split('.'))
print("1. 2. 3. 4. 5. 6".split('. '))
print("1 2 3 4 5 6".split(' '))
print("1 \n2 \t3 4 \n\t5 6".split())