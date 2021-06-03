file = open('chicken.txt', 'r', encoding='utf-8')
sum = 0
for i in file:
    data = i.split(': ')
    print('날짜 :', data[0], ', 매출액 :', data[1]) #날짜, 금액
    sum += int(data[1])
print(f"\n매출액 합계: {sum}")
file.close()
print("========================")
file = open('chicken.txt', 'r', encoding='utf-8')
sum = 0
for i in file:
    # strip(); 공란 \n, \t 제거
    data = i.strip().split(': ')
    print('날짜 :', data[0], ', 매출액 :', data[1]) #날짜, 금액
    sum += int(data[1])
print(f"매출액 합계: {sum}")
file.close()